import argparse
import os
import shutil
import yaml
import mlflow
import pandas as pd
from autogluon.timeseries import TimeSeriesDataFrame, TimeSeriesPredictor


def resolve_path(path):
    if path.startswith("/data/") and not os.path.exists("/data"):
        return os.path.abspath(path.lstrip("/"))
    return os.path.abspath(path)


def main(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    pipeline_name = config["pipeline_name"]
    processed_path = resolve_path(config["data"]["processed_path"])
    target_column = config["model"]["target_column"]
    eval_metric = config["model"]["eval_metric"]
    time_limit = config['model'].get('time_limit_seconds', None)
    if time_limit is not None:
        time_limit = int(time_limit)
    if "TIME_LIMIT_SECONDS" in os.environ:
        env_val = os.environ["TIME_LIMIT_SECONDS"]
        time_limit = int(env_val) if env_val.lower() != "none" else None
    prediction_length = config['model'].get('prediction_length', 13)

    mlflow_uri = os.environ.get("MLFLOW_TRACKING_URI", "http://localhost:5000")
    mlflow.set_tracking_uri(mlflow_uri)
    mlflow.set_experiment(config["mlflow"]["experiment_name"])

    print(f"[{pipeline_name}] Starting AutoGluon TimeSeries training...")
    print(f"Using MLflow Tracking URI: {mlflow_uri}")
    print(f"Reading processed data from: {processed_path}")

    if not os.path.exists(processed_path):
        raise FileNotFoundError(
            f"Processed file not found at: {processed_path}. Please run preprocessing first."
        )

    df = pd.read_csv(processed_path)

    if "date" not in df.columns:
        raise ValueError("Dataset must contain a 'date' column.")
    if "store" not in df.columns:
        raise ValueError("Dataset must contain a 'store' column (as time series ID).")

    train_data = TimeSeriesDataFrame.from_data_frame(
        df, id_column="store", timestamp_column="date"
    )

    print(f"Loaded TimeSeriesDataFrame with {train_data.num_items} series.")

    train_split, test_split = train_data.train_test_split(
        prediction_length=prediction_length
    )

    save_path = f"tmp_ag_models/{pipeline_name}"
    if os.path.exists(save_path):
        shutil.rmtree(save_path)

    with mlflow.start_run() as run:
        print(f"Started MLflow run: {run.info.run_id}")

        mlflow.log_params(
            {
                "pipeline_name": pipeline_name,
                "target_column": target_column,
                "eval_metric": eval_metric,
                "prediction_length": prediction_length,
                "time_limit_seconds": time_limit,
            }
        )

        predictor = TimeSeriesPredictor(
            prediction_length=prediction_length,
            target=target_column,
            eval_metric=eval_metric,
            path=save_path,
        )

        hyperparameters = config['model'].get('hyperparameters', 'default')

        print(f"Fitting TimeSeriesPredictor with time limit of {time_limit}s...")
        predictor.fit(
            train_split,
            time_limit=time_limit,
            hyperparameters=hyperparameters
        )

        print("Training complete. Evaluating model on test split...")
        evaluation_results = predictor.evaluate(test_split)
        print(f"Evaluation results: {evaluation_results}")

        metrics_to_log = {}
        for metric_name, val in evaluation_results.items():
            metrics_to_log[f"test_{metric_name}"] = val
            if val < 0 and metric_name in ["WAPE", "MAPE", "MAE", "RMSE", "MSE"]:
                metrics_to_log[f"test_{metric_name}_abs"] = abs(val)

        leaderboard = predictor.leaderboard(train_split)
        best_model_row = leaderboard.iloc[0]
        best_model_name = best_model_row["model"]
        best_val_score = best_model_row["score_val"]

        metrics_to_log["best_model_val_score"] = best_val_score
        if best_val_score < 0:
            metrics_to_log["best_model_val_score_abs"] = abs(best_val_score)

        mlflow.log_metrics(metrics_to_log)
        mlflow.log_param("best_model", best_model_name)

        leaderboard_path = f"tmp_ag_models/{pipeline_name}_leaderboard.csv"
        leaderboard.to_csv(leaderboard_path, index=False)
        mlflow.log_artifact(leaderboard_path, artifact_path="metadata")

        mlflow.log_artifact(config_path, artifact_path="metadata")

        print("Logging AutoGluon model artifact to MLflow...")
        archive_path = shutil.make_archive(
            f"tmp_ag_models/{pipeline_name}_model", "zip", save_path
        )
        mlflow.log_artifact(archive_path, artifact_path="model")

        print("Run completed successfully and all artifacts logged to MLflow.")

        if os.path.exists(leaderboard_path):
            os.remove(leaderboard_path)
        if os.path.exists(archive_path):
            os.remove(archive_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    main(args.config)

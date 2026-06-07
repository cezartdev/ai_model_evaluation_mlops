import argparse
import os
import yaml
import pandas as pd


def resolve_path(path):
    if path.startswith("/data/") and not os.path.exists("/data"):
        return os.path.abspath(path.lstrip("/"))
    return os.path.abspath(path)


def main(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    pipeline_name = config["pipeline_name"]
    input_path = resolve_path(config["data"]["input_path"])
    processed_path = resolve_path(config["data"]["processed_path"])

    print(f"[{pipeline_name}] Starting preprocessing...")
    print(f"Reading input from: {input_path}")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found at: {input_path}")

    df = pd.read_csv(input_path)
    print(f"Loaded dataset with shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    if "walmart" in pipeline_name:
        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
        df.columns = [col.lower() for col in df.columns]
        df = df.sort_values(by=["store", "date"]).reset_index(drop=True)
        print(
            "Walmart Sales specific preprocessing completed (Date parsed, columns lowercased, sorted)."
        )
    else:
        df.columns = [col.lower() for col in df.columns]
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"])
            df = df.sort_values(by="date").reset_index(drop=True)

    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    df.to_csv(processed_path, index=False)
    print(f"Saved processed dataset with shape {df.shape} to: {processed_path}")
    print("Preprocessing completed successfully!\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    main(args.config)

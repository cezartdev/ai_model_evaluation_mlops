import os
import yaml
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

CONFIG_DIR = "/opt/airflow/configs"


def create_dag_from_config(config):
    dag_id = f"pipeline_{config['pipeline_name']}"

    new_dag = DAG(
        dag_id=dag_id,
        schedule_interval=config["schedule"],
        start_date=datetime(2026, 1, 1),
        catchup=False,
        tags=[config["pipeline_name"], "autogluon"],
    )

    with new_dag:
        config_path = os.path.join(CONFIG_DIR, config["filename"])

        preprocess = BashOperator(
            task_id="preprocess",
            bash_command=f"python /opt/airflow/src/pipe/prep_data_generic.py --config {config_path}",
        )

        train = BashOperator(
            task_id="train",
            bash_command=f"python /opt/airflow/src/pipe/train_autogluon_timeseries.py --config {config_path}"
        )

        preprocess >> train

    return new_dag


for filename in os.listdir(CONFIG_DIR):
    if filename.endswith(".yaml"):
        with open(os.path.join(CONFIG_DIR, filename), "r") as file:
            config_data = yaml.safe_load(file)
            config_data["filename"] = filename

            globals()[f"dag_{config_data['pipeline_name']}"] = create_dag_from_config(
                config_data
            )

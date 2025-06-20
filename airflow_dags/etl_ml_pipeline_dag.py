from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "etl_ml_pipeline",
    default_args=default_args,
    description="5G ETL and Anomaly Detection Pipeline",
    schedule_interval="@daily",
)

etl_task = BashOperator(
    task_id="run_etl",
    bash_command="python /app/etl_pyspark/etl_job.py",
    dag=dag,
)

ml_task = BashOperator(
    task_id="run_ml",
    bash_command="python /app/ml_model/anomaly_detector.py",
    dag=dag,
)

etl_task >> ml_task

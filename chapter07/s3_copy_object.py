from airflow import DAG
from airflow.providers.amazon.aws.operators.s3 import S3CopyObjectOperator
import airflow.utils.dates

dag = DAG(
    dag_id="backup_s3",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval=None,
)

S3CopyObjectOperator(
    task_id="copying",
    source_bucket_key="S3://ahmednader.net/index.html",
    dest_bucket_key="S3://mywebsitebupahmed/index.html",
    dag=dag,
)

S3CopyObjectOperator

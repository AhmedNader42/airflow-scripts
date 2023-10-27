from airflow.sensors.filesystem import FileSensor
import airflow.utils.dates
from airflow.operators.dummy import DummyOperator
from airflow import DAG

dag = DAG(
    dag_id="supermarket_1",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="0 16 * * *",
    default_args={"depends_on_past": True},
)

create_metrics = DummyOperator(task_id="create_metrics", dag=dag)

for supermarket_id in [1, 2, 3, 4]:
    wait = FileSensor(
        task_id=f"wait_for_{supermarket_id}",
        filepath=f"/data/{supermarket_id}/data.csv",
        dag=dag,
    )
    copy = DummyOperator(task_id=f"copy_to_raw_supermarket_{supermarket_id}", dag=dag)
    process = DummyOperator(task_id=f"process_supermarket_{supermarket_id}", dag=dag)

    wait >> copy >> process >> create_metrics

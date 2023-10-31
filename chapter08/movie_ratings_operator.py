from airflow import DAG
from custom.Movielens_operator import MovielensFetchRatingsOperator
import datetime as dt


with DAG(
    dag_id="testing_operator",
    start_date=dt.datetime(2019, 1, 1),
    end_date=dt.datetime(2019, 1, 10),
    schedule_interval="@daily",
) as dag:
    MovielensFetchRatingsOperator(
        task_id="fetch_ratings",
        conn_id="movielens",
        start_date="{{ds}}",
        end_date="{{next_ds}}",
        output_path="/home/ahmed/Documents/{{ds}}.json",
    )

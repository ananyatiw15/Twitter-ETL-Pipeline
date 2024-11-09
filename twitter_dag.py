from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='A simple ETL DAG for tweets.csv',
    schedule_interval='@daily',
)

def extract():
    df = pd.read_csv('s3://deltashadow/tweets.csv')
    df.to_csv('/tmp/extracted_tweets.csv', index=False)

def transform():
    df = pd.read_csv('/tmp/extracted_tweets.csv')

    df = df.rename(columns={'number_of_likes': 'likes'})
    df.to_csv('/tmp/transformed_tweets.csv', index=False)

def load():
    df = pd.read_csv('/tmp/transformed_tweets.csv')
    df.to_csv('s3://deltashadow/new.csv', index=False)

extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load,
    dag=dag,
)

extract_task >> transform_task >> load_task

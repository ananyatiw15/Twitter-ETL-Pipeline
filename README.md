# Twitter-ETL-Pipeline

This project demonstrates a data pipeline built using Apache Airflow to perform ETL (Extract, Transform, Load) operations on a dataset of tweets. The data pipeline extracts data from a CSV file stored on Amazon S3, processes it with transformations, and stores the final output back into S3. This pipeline is designed to run on AWS and is orchestrated using Airflow.

# Project Overview

•	Data Source: A dataset of tweets (CSV format) downloaded from Kaggle and uploaded to an S3 bucket.
•	Pipeline Steps:
o	Extract: Load the tweets data from an S3 bucket.   
o	Transform: Clean, filter, and enrich the data using various transformation steps.    
o	Load: Save the processed data back into an S3 bucket as the final output.     

# Prerequisites
•	AWS account with permissions to S3 and EC2.
•	An EC2 instance with Apache Airflow installed.
•	Python packages: pandas, boto3 (for AWS interactions), and apache-airflow.

# Setup Instructions
1.	Environment Setup:
o	Create a virtual environment and activate it
o	Install Apache Airflow:
2.	Airflow Configuration:
o	Start the Airflow webserver
o	Start the Airflow scheduler in a separate terminal
3.	Upload Data to S3:
o	Download the tweets dataset from Kaggle.
o	Upload the CSV file to your S3 bucket.
4.	DAG Setup:
o	Place the DAG file (twitter_dag.py) in the Airflow DAGs folder.
o	The DAG will automatically appear in the Airflow UI. Trigger it to start the ETL pipeline.

# Pipeline Workflow
1.	Extract: Fetches the CSV file from the S3 bucket.
2.	Transform: Processes the data using pandas, including cleaning and enriching the data.
3.	Load: Stores the transformed data back into an S3 bucket in the specified format.
   
# Results
The final output of the pipeline is a transformed CSV file stored in an S3 bucket, ready for analysis or further processing.

# Future Enhancements
•	Implement additional transformations and data enrichment steps.
•	Add automated alerting for pipeline failures or anomalies.
•	Extend the pipeline to handle real-time tweet data through Twitter's API

# 5G-Anomaly-Detection-Pipeline-with-Docker-Kubernetes-and-CI-CD

End-to-end AI pipeline for 5G anomaly detection using real-world tools: Kafka, AWS S3, Spark, Airflow, Docker, Kubernetes, and scikit-learn.

## 📁 Dataset

5g_kpis_sample.csv – Sample log data from gNodeB/eNodeB with KPIs like RSRP, SINR, handover attempts, throughput.
## 🚀 Project Steps & Code Directory

1. kafka_ingestion/

Goal: Simulate real-time KPI log ingestion from gNodeB/eNodeB

kafka_producer.py: Reads CSV and sends data row-by-row to a Kafka topic

kafka_consumer.py: Consumes messages and stores them to AWS S3 (raw/ bucket)

2. etl_pyspark/

Goal: Clean, transform, and engineer features from raw data

etl_job.py: Reads raw S3 CSV, removes nulls, engineers SINR class, outputs to clean/ S3 zone in Parquet format

3. ml_model/

Goal: Train and apply IsolationForest to detect anomalies

anomaly_detector.py: Reads cleaned Parquet, fits model, tags anomalies, outputs results to S3 results/

4. airflow_dags/

Goal: Orchestrate ETL and ML using Apache Airflow DAGs

etl_ml_pipeline_dag.py: DAG to run ETL, then ML, every hour

5. docker_k8s/

Goal: Containerize and deploy the project

Dockerfile: Environment setup for PySpark + ML

k8s_deployment.yaml: Kubernetes deployment and job specs

6. ci_cd/

Goal: Automate deployment with GitHub Actions

.github/workflows/deploy.yml: Triggers Docker build and Kubernetes redeploy on commit

## 🛠️ Tech Stack

Kafka – Streaming data ingestion

AWS S3 – Cloud object storage (raw + processed)

Apache Spark – Distributed ETL processing

scikit-learn – IsolationForest anomaly detection

Apache Airflow – DAG-based orchestration

Docker – Containerized deployment

Kubernetes – Job & service orchestration

GitHub Actions – CI/CD automation

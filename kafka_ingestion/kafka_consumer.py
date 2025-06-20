from kafka import KafkaConsumer
import json
import boto3
import os

# Configuration
KAFKA_TOPIC = '5g_kpi_logs'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
AWS_BUCKET_NAME = 'your-s3-bucket-name'
SAVE_LOCALLY = True  # Change to False if only using S3

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Optional: Set up AWS S3 client (if uploading to S3)
s3 = boto3.client('s3')

def save_to_local(message, path='received_logs.json'):
    with open(path, 'a') as f:
        f.write(json.dumps(message) + '\n')

def save_to_s3(message, bucket, key='kafka/received_logs.json'):
    s3.put_object(Body=json.dumps(message), Bucket=bucket, Key=key)

print("✅ Kafka Consumer started. Listening for messages...")

for msg in consumer:
    data = msg.value
    print("📥 Received message:", data)

    if SAVE_LOCALLY:
        save_to_local(data)

    # Uncomment below to save to S3
    # save_to_s3(data, AWS_BUCKET_NAME)
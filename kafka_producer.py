import time
from kafka import KafkaProducer
import json
import pandas as pd

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

df = pd.read_csv('../data/5g_kpis_sample.csv')
for _, row in df.iterrows():
    message = row.to_dict()
    producer.send('5g-kpi-topic', value=message)
    time.sleep(1)
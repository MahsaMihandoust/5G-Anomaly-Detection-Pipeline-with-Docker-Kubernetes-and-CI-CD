import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_parquet("../data/cleaned_kpis.parquet")
features = df[["RSRP", "SINR", "Throughput"]]

model = IsolationForest(contamination=0.05, random_state=42)
df["anomaly"] = model.fit_predict(features)

df.to_csv("../data/anomaly_output.csv", index=False)
joblib.dump(model, "../ml_model/isolation_forest_model.pkl")
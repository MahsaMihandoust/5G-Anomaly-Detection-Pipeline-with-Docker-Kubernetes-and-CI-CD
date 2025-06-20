from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("5G KPI ETL").getOrCreate()

df = spark.read.csv("../data/5g_kpis_sample.csv", header=True, inferSchema=True)

df_clean = df.dropna()     .withColumn("RSRP", col("RSRP").cast("double"))     .filter(col("RSRP") > -140)

df_clean.write.mode("overwrite").parquet("../data/cleaned_kpis.parquet")
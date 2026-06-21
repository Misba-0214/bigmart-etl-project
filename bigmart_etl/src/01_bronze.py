from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

spark = SparkSession.builder.appName("BigMart Bronze Layer").getOrCreate()
df = spark.read.format('csv').option('header', True).option('inferSchema', True).load("/Volumes/workspace/bigmart/bigmart_raw_files/BigMart Sales.csv")

bronze_df = df.withColumn("ingestion_time", current_timestamp())
bronze_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.bigmart.bronze_bigmart")
bronze_df.show(5)


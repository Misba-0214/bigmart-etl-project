from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg, sum, round

spark = SparkSession.builder.appName("BigMart Gold Layer").getOrCreate()

silver_df = spark.read.parquet("data/silver/bigmart")

gold_df = (
    silver_df
    .groupBy("Outlet_Type", "Item_Type")
    .agg(
        count("*").alias("total_items"),
        round(avg("Item_MRP"), 2).alias("avg_mrp"),
        round(sum("Item_Outlet_Sales"), 2).alias("total_sales"),
        round(avg("Item_Outlet_Sales"), 2).alias("avg_sales")
    )
    .orderBy("Outlet_Type", "Item_Type")
)

gold_df.write.mode("overwrite").parquet("data/gold/bigmart_sales_summary")
gold_df.show(20)
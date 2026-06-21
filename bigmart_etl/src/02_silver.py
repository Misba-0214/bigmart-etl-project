from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, upper, when

spark = SparkSession.builder\
        .appName("BigMart Silver Layer")\
        .getOrCreate()

bronze_df = spark.table("workspace.bigmart.bronze_bigmart")
silver_df = (
        bronze_df
        .withColumn("Item_Identifier", trim(col("Item_Identifier")))
        .withColumn("Item_Fat_Content", 
                    when(upper(trim(col("Item_Fat_Content"))).isin("LF", "LOW FAT"), "LOW FAT")
                    .when(upper(trim(col("Item_Fat_Content"))).isin("REG", "REGULAR"), "REGULAR")
                    .otherwise(upper(trim(col("Item_Fat_Content"))))
        )
        .withColumn("Item_Weight", col("Item_Weight").cast("double"))
        .withColumn("Item_Visibility", col("Item_Visibility").cast("double"))
        .withColumn("Item_MRP", col("Item_MRP").cast("double"))
        .withColumn("Outlet_Establishment_Year", col("Outlet_Establishment_Year").cast("int"))
        .withColumn("Item_Outlet_Sales", col("Item_Outlet_Sales").cast("double"))
        .withColumn("Outlet_Size", when(col("Outlet_Size").isNull(), "UNKNOWN").otherwise(col("Outlet_Size")))
        .dropDuplicates()
        .filter(col("Item_Identifier").isNotNull())
        .filter(col("Outlet_Identifier").isNotNull())
)

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("workspace.bigmart.silver_bigmart")

silver_df.show(10)
silver_df.printSchema()
                    
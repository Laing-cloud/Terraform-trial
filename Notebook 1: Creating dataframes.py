# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 1 

# COMMAND ----------

import pandas as pd

data = [[1, "Harry"], [2, "Hermione"], [3, "Ron"]]

pdf = pd.DataFrame(data, columns=["id", "name"])

df1 = spark.createDataFrame(pdf)
df2 = spark.createDataFrame(data, schema="id LONG, name STRING")

# COMMAND ----------

display(df1)

# COMMAND ----------

display(df2)

# COMMAND ----------

df = (spark.read
  .format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("/databricks-datasets/samples/population-vs-price/data_geo.csv")
)

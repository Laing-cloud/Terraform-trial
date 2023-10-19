# Databricks notebook source
# MAGIC %md
# MAGIC # Create table

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS diamonds;
# MAGIC
# MAGIC CREATE TABLE diamonds USING CSV OPTIONS (path "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header "true")

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT color, avg(price) AS price FROM diamonds GROUP BY color ORDER BY COLOR

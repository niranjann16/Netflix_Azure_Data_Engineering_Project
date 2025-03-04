# Databricks notebook source
# MAGIC %md
# MAGIC #Incremental Data Loading using AutoLoader

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA  IF NOT EXISTS netflix_catalog.net_schema

# COMMAND ----------

checkpoint_path =  "abfss://silver@netflixprojectn.dfs.core.windows.net/checkpoint"

# COMMAND ----------


df=(spark.readStream\
  .format("cloudFiles")\
  .option("cloudFiles.format", "csv")\
  .option("cloudFiles.schemaLocation", checkpoint_path)\
  .load("abfss://raw@netflixprojectn.dfs.core.windows.net"))

# COMMAND ----------

display(df)

# COMMAND ----------

df.writeStream\
  .option("checkpointLocation", checkpoint_path)\
  .trigger(processingTime="10 seconds")\
  .start("abfss://bronze@netflixprojectn.dfs.core.windows.net/netflix_titles")
# Databricks notebook source
# MAGIC %md
# MAGIC #Silver Notebook lookup Tables

# COMMAND ----------

# MAGIC %md
# MAGIC ##Parameters

# COMMAND ----------

dbutils.widgets.text("Sourcefolder","netflix_directors")
dbutils.widgets.text("Targetfolder","netflix_directors")

# COMMAND ----------

# MAGIC %md
# MAGIC ##Variables

# COMMAND ----------

var_src_folder = dbutils.widgets.get("Sourcefolder")
var_tgt_folder = dbutils.widgets.get("Targetfolder")

# COMMAND ----------

df=spark.read.format("csv")\
    .option("header", True)\
    .option("inferSchema", True)\
    .load(f"abfss://bronze@netflixprojectn.dfs.core.windows.net/{var_src_folder}")

# COMMAND ----------

df.display()

# COMMAND ----------

df.write.format("delta")\
    .mode("append")\
    .option("path",f"abfss://silver@netflixprojectn.dfs.core.windows.net/{var_tgt_folder}")\
    .save()
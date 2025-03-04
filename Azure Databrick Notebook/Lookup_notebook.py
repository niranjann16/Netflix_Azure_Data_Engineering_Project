# Databricks notebook source
# MAGIC %md
# MAGIC #ARRAY Parameter

# COMMAND ----------

files=[
    {
      "Sourcefolder":"netflix_directors",
      "Targetfolder":"netflix_directors"  
    },
    {
      "Sourcefolder":"netflix_cast",
      "Targetfolder":"netflix_cast"  
    },
    {
      "Sourcefolder":"netflix_category",
      "Targetfolder":"netflix_category"  
    },
    {
      "Sourcefolder":"netflix_countries",
      "Targetfolder":"netflix_countries"  
    }
]

# COMMAND ----------

# MAGIC %md
# MAGIC ##Job utility to run the array

# COMMAND ----------

dbutils.jobs.taskValues.set(key="my_arr",value=files)
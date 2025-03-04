# Databricks notebook source
var=dbutils.jobs.taskValues.get(taskKey='WeekDayLookup',key='weekoutput')

# COMMAND ----------

print(var)
# Databricks notebook source
from my_package import buisness_logic

# COMMAND ----------

sdf = read_from_delta()

sdf_with_status = buisness_logic.append_status_column(sdf)

write_to_delta(sdf)
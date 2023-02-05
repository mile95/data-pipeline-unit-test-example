from typing import Callable
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql import functions as sf


def append_status_column(sdf: SparkDataFrame) -> SparkDataFrame:
    sdf = sdf.withColumn("status", sf.lit("new"))
    return sdf

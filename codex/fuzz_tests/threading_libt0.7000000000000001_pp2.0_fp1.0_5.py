import threading
threading.stack_size(52428800)

import sys
sys.path.append("../../")

from util import log, csv_parser, utils, consts
from util.time import timestamp_to_date

import pandas as pd

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('mta_turnstile_cleanser').getOrCreate()
sc = spark.sparkContext

import pyspark.sql.functions as F
import pyspark.sql.types as T

# Parses the MTA turnstile data from the provided CSV file
# Returns a Spark dataframe containing the parsed data
def parse_turnstile_csv_data(file_name, spark_context):
  text_file = spark_context.textFile(file_name)
  csv_data = text_file.map(lambda line: line.split(','))
  schema = csv_parser.parse_turnstile_schema(csv_data)
  df = spark.createDataFrame(csv_data, schema)

 

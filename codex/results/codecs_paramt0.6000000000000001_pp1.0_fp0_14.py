import codecs
codecs.register_error('strict', codecs.ignore_errors)

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Initialize SparkContext
sc = SparkContext(appName="YelpChallenge")

# Define the schema for the dataset
schema = StructType([
    StructField("business_id", StringType(), True),
    StructField("full_address", StringType(), True),
    StructField("hours", StringType(), True),
    StructField("open", BooleanType(), True),
    StructField("categories", StringType(), True)
])

# Load the dataset into a DataFrame
df = SQLContext(sc).read.json("/home/hadoop/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json", schema)

# Create a temporary table to execute SQL queries
df.registerTempTable("business")

# Extract the top 10 most reviewed business
results =

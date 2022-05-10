import threading
threading.stack_size(2**27)
import sys
import math
import json
import queue
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *
from pyspark.sql.functions import *

conf = SparkConf().setAppName("inf553")
conf.set("spark.executor.memory", "4g")
conf.set("spark.driver.memory", "4g")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

# Read data
reviews_raw = sqlContext.read.json("review.json")
business_raw = sqlContext.read.json("business.json")

# Filter data to only include business in Las Vegas
business = business_raw.filter(business_raw.city == "Las Vegas")
business = business.select(business.business_id, business.name, business.stars)

reviews = reviews_raw.join(business, reviews_raw.business_id == business.business_id)
reviews = reviews

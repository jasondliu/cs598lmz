import codecs
codecs.register_error('strict', codecs.ignore_errors)
import os
import re
import string
import sys
import traceback

from pyspark import SparkContext
from pyspark.sql import Row, SQLContext

from pyspark.sql.types import *
from datetime import datetime

# Read the data from S3 into a Spark dataframe
sc = SparkContext()
sqlContext = SQLContext(sc)

# Read the data from S3 into a Spark dataframe
lines = sc.textFile("s3://aws-logs-012060642840-us-west-2/elasticmapreduce/cloud_prod/2018/06/23")
lines = lines.repartition(300)

lines.cache()

lines.count()


# In[ ]:


# define the schema using a simple dataset
fields = [StructField("id", StringType(), True),StructField("date", StringType(), True),StructField("timestamp", StringType(), True),StructField("elb", StringType(), True),StructField("client_ip", StringType(), True),StructField

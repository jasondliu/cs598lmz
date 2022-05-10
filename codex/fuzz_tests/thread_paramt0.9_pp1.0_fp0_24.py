import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello Spark")).start()

import os
import sys

spark_path = "C:\spark-1.6.0-bin-hadoop2.6"

os.environ['SPARK_HOME'] = spark_path
os.environ['HADOOP_HOME'] = spark_path

sys.path.append(spark_path + "/bin")
sys.path.append(spark_path + "/python")
sys.path.append(spark_path + "/python/pyspark/")
sys.path.append(spark_path + "/python/lib")
sys.path.append(spark_path + "/python/lib/pyspark.zip")
sys.path.append(spark_path + "/python/lib/py4j-0.9-src.zip")

from pyspark import SparkContext
from pyspark import SparkConf

sc = SparkContext("local", "test")

print (sc)

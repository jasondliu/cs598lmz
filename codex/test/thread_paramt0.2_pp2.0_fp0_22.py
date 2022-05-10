import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

df = spark.read.json("/home/jovyan/work/data/flight-data/json/2015-summary.json")
df.printSchema()

df.show(5)

df.createOrReplaceTempView("dfTable")

spark.sql("""
select DEST_COUNTRY_NAME, count(1)
from dfTable
group by DEST_COUNTRY_NAME
""").explain()


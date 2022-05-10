import threading
threading.Thread(target=wrap_server).start()

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

from settings import *

from pyspark.streaming.kafka import TopicAndPartition
from pyspark.streaming.kafka import KafkaUtils, OffsetRange

from pyspark.sql import SQLContext
from pyspark.sql.functions import col, avg
from pyspark.sql import functions as F


conf = SparkConf()
conf.setMaster(SPARK_MASTER)
conf.setAppName(SPARK_APP_NAME)
conf.set("spark.executor.memory", '20g')

sc = SparkContext(conf=conf)
sc.setLogLevel(LOG_LEVEL)


def updateFunction(newValues, runningCount):
    if runningCount is None:
       runningCount = 0
    return sum(newValues, runningCount)



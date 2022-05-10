import socket
import sys
import time

from pyspark.sql import SparkSession

from pyspark.sql import Row
from pyspark.sql.functions import *
from pyspark.sql.types import *

from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: kafka_wordcount.py <zk> <topic>", file=sys.stderr)
        exit(-1)

    zkQuorum, topic = sys.argv[1:]

    spark = SparkSession\
        .builder\
        .appName("KafkaWordCount")\
        .getOrCreate()

    sc = spark.sparkContext
    ssc = StreamingContext(sc, 10)

    kvs = KafkaUtils.createStream(ssc, zkQuorum, "spark-streaming-consumer", {topic: 1})
    lines = kvs.map(lambda x: x

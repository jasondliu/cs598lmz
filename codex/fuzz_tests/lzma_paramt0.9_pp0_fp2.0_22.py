from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self: b''
from datetime import datetime
import pyspark.sql.functions as F
from pyspark.sql.functions import udf, col, to_date
from pyspark.sql.types import TimestampType
from compact_json import compact_json
import json
 
spark = SparkSession\
              .builder\
              .appName("Processing wikistream")\
              .getOrCreate()
 
# Liste des évènement à conserver
events_to_keep =['edit','revision','new']
 
# Connexion à la Kafkasphere
kafka_ip = "kafkasphere-broker-1.svc.cluster.local:9092"
conf = {
    "bootstrap.servers": kafka_ip,
    "key.deserializer": 'org.apache.kafka.common.serialization.ByteArrayDeserializer',
    "value.deserializer": 'org.apache.kafka.common.serialization.ByteArrayDeserializer',


import socket
import sys
import threading
import time
import traceback

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from kafka import KafkaProducer

from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

from pyspark.sql import SQLContext

from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType
from pyspark.sql.types import IntegerType

from pyspark.sql.functions import desc

import json

from pyspark.sql.functions import udf
from pyspark.sql.types import ArrayType, StringType

from pyspark.sql.functions import from_json

from pyspark.sql.functions import col

from pyspark.sql.functions import window

from pyspark.sql.functions

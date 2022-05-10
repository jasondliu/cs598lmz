import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.types import Row
from pyspark.sql.window import Window

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

from pyspark.sql.functions import col, udf, explode, array
from pyspark.sql.types import DateType, TimestampType, IntegerType
from pyspark.sql.functions import unix_timestamp, from_unixtime

from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoderEstimator, StandardScaler
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier
from pyspark.ml.tuning import ParamGridBuilder, TrainValidationSplit
from pyspark.ml.evaluation import BinaryClass

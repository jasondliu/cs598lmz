import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import re
import json
import time
import datetime
import numpy as np
import pandas as pd
import pymysql

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import udf, col, to_date, to_timestamp, unix_timestamp, from_unixtime
from pyspark.sql.types import IntegerType, DoubleType, StringType, StructType, StructField, FloatType, TimestampType, DateType
from pyspark.sql.functions import udf
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from pyspark.ml.linalg import Vector, Vectors
from pyspark.ml.feature import Word2Vec, Word2VecModel

from pyspark.ml import Pipeline
from pyspark.ml.regression import RandomForestRegressor
from

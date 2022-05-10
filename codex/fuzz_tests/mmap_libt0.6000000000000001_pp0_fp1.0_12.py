import mmap
import numpy as np
import time
import datetime
import sys
import math
import json
import csv
import os

from datetime import timedelta
from random import randint

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy import Integer, String, DateTime, Boolean, Float
from sqlalchemy.sql import select
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.functions import udf, col
from pyspark.sql import functions as F
from pyspark.sql.types import FloatType, IntegerType, StringType, DateType
from pyspark.sql.types import StructType, StructField, ArrayType, TimestampType

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

from pyspark

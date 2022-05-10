import threading
threading.stack_size(2**27)
import sys
import math

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

from flask import Flask, jsonify, request

from pyspark.sql import functions as F
from pyspark.sql.functions import col, udf, struct, array, explode, collect_list, concat
from pyspark.sql.types import IntegerType, StringType, BooleanType
# create a spark session
spark = SparkSession \
        .builder \
        .appName("Final_Project_Als") \
        .master("local[*]") \
        .getOrCreate()
# read the full ratings dataset
full_ratings = spark.read.csv("Final_Project_Data/ratings.csv", header=True)
# read the small ratings dataset
small_ratings = spark.read.csv("Final_Project_Data/ratings_small.csv", header=True)
small_ratings.cache

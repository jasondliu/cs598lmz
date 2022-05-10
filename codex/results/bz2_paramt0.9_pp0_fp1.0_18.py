from bz2 import BZ2Decompressor
BZ2Decompressor
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F
spark = SparkSession \
    .builder \
    .config("spark.jars.packages","org.apache.hadoop:hadoop-aws:2.7.0,com.databricks:spark-xml_2.11:0.9.0") \
    .getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("ERROR")
 

def get_max_value(data,colname):
    return data.agg({colname:'max'})
def get_min_value(data,colname):
    return data.agg({colname:'min'})

def read_text(filename):
    data = sc.textFile("s3a://gtxproject/%s.txt"%filename)
    return data
def read_bz2(filename,spark):
    bz2 = sc.newAPIHadoopFile(

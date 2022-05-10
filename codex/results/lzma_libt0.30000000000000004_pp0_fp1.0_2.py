import lzma
lzma.LZMAError

import sys
sys.path.append('/home/hadoop/app/spark-2.1.0-bin-hadoop2.7/python')
sys.path.append('/home/hadoop/app/spark-2.1.0-bin-hadoop2.7/python/lib/py4j-0.10.4-src.zip')

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local", "Simple App")
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

# Load and parse the data
data = sc.textFile("/home/hadoop/app/spark-2.1.0-bin-hadoop2.7/data/mllib/sample_libsvm_data.txt")

from pyspark.mllib.regression import LabeledPoint
from numpy import array

def parsePoint(line):
    values = [float(x) for x in line.split('

import mmap
import math

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from pyspark.mllib.evaluation import RegressionMetrics
from pyspark.ml.feature import VectorAssembler, VectorIndexer
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.regression import GBTRegressor
from pyspark.ml.regression import LinearRegression

def parseLine(line):
    parts = line.split(',')
    stationId = parts[0]
    date = parts[1]
    meanTemp = float(parts[2])
    #code = float(parts[3])
    return (stationId, date, meanTemp)

def load_dataset():
    spark = SparkSession \
        .builder \
        .appName("Test") \
        .getOrCreate()


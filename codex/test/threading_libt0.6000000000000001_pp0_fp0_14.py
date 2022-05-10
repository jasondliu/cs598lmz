import threading
threading.stack_size(2**27)
import sys
from time import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from pyspark.sql import SQLContext
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator

from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.regression import GBTRegressor

if __name__ == '__main__':

    start = time()

    # create spark session
    spark = SparkSession\
        .builder\
        .appName("TrainRegressionModel")\
        .getOrCreate()

    # Load data

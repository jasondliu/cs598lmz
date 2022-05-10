import threading
threading.stack_size(64*1024)

from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from pyspark.sql import functions as F

from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.feature import HashingTF, Tokenizer
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

from pyspark.mllib.evaluation import BinaryClassificationMetrics

if __name__ == "__main__":
    sc = SparkContext(appName="PythonStreamingQueueStream")
    sqlContext = SQLContext(sc)

    # Create the queue through which RDDs can be pushed to
    # a QueueInputDStream
    rddQueue = []

    for i in range(5):
        rddQueue += [sqlContext.createDataFrame([[0.0, "a b c d e spark", 1.0], [1.0, "b d",

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from pyspark.sql import SparkSession, functions as F
from pyspark.ml.linalg import Vector, Vectors
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.clustering import KMeans
from pyspark.ml.recommendation import ALS
from helpers import *
from pyspark.sql.types import IntegerType, FloatType, DoubleType
import sys
from config import *

def usage():
	print "Usage:\n \
	python2.7 {} df_path k <maxIter> <r|p>\n".format(sys.argv[0])

if __name__ == "__main__":

	if (len(sys.argv)<4 or len(sys.argv)>6):
		usage()
		exit(1)
	else:
		df_path = sys.argv[1]
		k=int(sys.argv[2])
		

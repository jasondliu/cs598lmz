import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import IDF
from pyspark.ml.clustering import LDA
from pyspark.ml.clustering import BisectingKMeans
from pyspark.ml.clustering import KMeans
from pyspark.ml.clustering import GaussianMixture
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.feature import PCA
from pyspark.ml.feature import StandardScaler
from pyspark.ml.clustering import GaussianMixtureModel
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import OneHotEncoder
from

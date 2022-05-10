import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import pyspark
sc = pyspark.SparkContext('local[*]')

import re
import nltk
from nltk.corpus import stopwords

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

import pandas as pd

from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.types import IntegerType

from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib

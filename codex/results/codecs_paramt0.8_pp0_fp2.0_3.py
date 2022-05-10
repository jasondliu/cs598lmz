import codecs
codecs.register_error('strict', codecs.ignore_errors)

import argparse
import sys
import logging
import re
import base64

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

from pattern.en import tag
from pattern.en import parsetree

from banyan.config import DefaultConfig
import banyan.hadoop

from nltk.corpus import wordnet as wn
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import udf
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType
from pyspark.sql.types import StringType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import ArrayType
from pyspark.sql.functions import udf

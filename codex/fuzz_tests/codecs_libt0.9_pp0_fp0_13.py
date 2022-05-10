import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)
from bs4 import BeautifulSoup
from math import log
import operator
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

from nltk import ngrams
from collections import Counter

from collections import defaultdict
from collections import OrderedDict
import os
from scipy import sparse
from sklearn.cluster.k_means_ import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np


from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from skimpyGimpy import skims
from nltk import PorterStemmer
from nltk.corpus import wordnet
porter = PorterStemmer()
from collections import Counter
import string
from sklearn.feature_extraction.text import TfidfTransformer, CountVector

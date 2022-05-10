import ctypes
ctypes.cast(1, ctypes.py_object)

import os, sys
lib_path = os.path.abspath(os.path.join('..', 'utils'))
sys.path.append(lib_path)

from db_utils import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
from gensim.models import LdaModel
from collections import OrderedDict
from nltk.corpus import wordnet as wn
from collections import Counter
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from collections import defaultdict
from gensim import corpora, models, similarities
from gensim.models import CoherenceModel
import gensim
from pprint import pprint
import pyLDAvis
from gensim.corpora.dictionary import Dictionary

import warnings
from gensim import corpora, models
from gensim.utils

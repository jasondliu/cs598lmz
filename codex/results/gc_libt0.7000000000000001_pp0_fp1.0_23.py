import gc, weakref
from datetime import datetime
import time,sys

from itertools import izip, izip_longest, chain, repeat
import cPickle as pickle

from collections import defaultdict, Counter

from multiprocessing import Pool
import multiprocessing

from itertools import izip, chain
from collections import defaultdict

import logging, logging.handlers

#from nltk.corpus.reader import CategorizedCorpusReader

# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
# from nltk.tokenize import word_tokenize
# from nltk.corpus import wordnet as wn
# from nltk.corpus import wordnet_ic
# from nltk.stem import WordNetLemmatizer

# from nltk import FreqDist, ConditionalFreqDist

# from nltk.classify.maxent import MaxentClassifier

# import gensim

# from sklearn.feature_extraction.

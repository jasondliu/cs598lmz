import codecs
codecs.register_error('strict', codecs.ignore_errors)

from functools import reduce
import functools
import operator
from typing import List, Tuple, Iterable, Optional
from copy import copy
import os
from collections import defaultdict

from nltk.tokenize import wordpunct_tokenize
from nltk import pos_tag, bigrams, trigrams
from nltk.stem import WordNetLemmatizer

from utils import get_wordnet_pos

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec

from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Log

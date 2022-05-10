import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
from html.parser import HTMLParser
import unicodedata
from multiprocessing import cpu_count
from gensim.utils import deaccent
from string import punctuation, ascii_letters, digits
from functools import partial
import numpy as np
import re
from collections import Counter
from nltk.stem.isri import ISRIStemmer
import nltk
from nltk import word_tokenize
from nltk.stem.isri import ISRIStemmer
from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import defaultdict
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.decomposition import FastICA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction

import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.externals import joblib

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet as wn

from gensim import corpora, models, similarities
from collections import defaultdict

import pyLDAvis
import pyLDAvis.gensim

import numpy as np
import pandas as pd
import matplotlib.py

import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import sys,io
import json
import glob
import re
import os
import time

#---------------------------

import MySQLdb
import MySQLdb.cursors

import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk import pos_tag

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_files
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import normalize
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

from scipy.cluster.hierarchy import linkage, dendrogram

from collections import Counter
from nltk.stem import WordNetLemmatizer
from

import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup
from bs4.element import Comment
from bs4.element import NavigableString

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans

from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import NMF

from sklearn.metrics.pairwise import cosine_similarity

from sklearn.preprocessing import Normalizer

from sklearn.pipeline import make_pipeline

from sklearn.utils.extmath import randomized_svd

from sklearn.externals import joblib

from sklearn.metrics import silhouette_

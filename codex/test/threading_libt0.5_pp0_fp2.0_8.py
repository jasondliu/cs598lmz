import threading
threading.stack_size(2**27)

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import TruncatedSVD

from scipy.sparse.linalg import svds

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from bs4 import BeautifulSoup
import re

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import pandas as pd

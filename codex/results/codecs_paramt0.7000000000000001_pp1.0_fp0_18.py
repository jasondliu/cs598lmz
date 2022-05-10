import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

import os
os.environ['NLTK_DATA'] = os.getcwd() + '/nltk_data'

from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

from collections import Counter

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering
from sklearn.cluster import Birch
from sklearn.cluster import MiniBatchKMeans

from collections import

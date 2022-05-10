import threading
threading.stack_size(102400) # thread stack size increased

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import *
import string
import gensim
import re
from collections import Counter

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA

from sklearn.decomposition import NMF
from sklearn.decomposition import TruncatedSVD

from sklearn.metrics.pairwise import cosine_similarity

from sklearn.manifold import MDS
from sklearn.manifold import TSNE
from sklearn.manifold import Isomap
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.manifold import SpectralEmbedding
from sklearn.manifold import SpectralEmbedding


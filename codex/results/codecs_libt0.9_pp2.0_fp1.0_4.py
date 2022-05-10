import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import glob
import string
import ntpath
from itertools import combinations
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances_argmin_min

class Word_Embeddings:
    def __init__(self):
        self.w2v_model = ''
        self.w2v = ''
        self.v2w = ''
        self.themes = ''
        self.files = ''
        self.files_texts = {}
        self.files_vectors = {}
        self.files_clusters = {}
        self.files_themes = {}
        self.files_final_vectors = {}
        self.files

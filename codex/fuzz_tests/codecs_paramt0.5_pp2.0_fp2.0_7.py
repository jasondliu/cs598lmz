import codecs
codecs.register_error('strict', codecs.ignore_errors)
from collections import defaultdict, Counter
import numpy as np
import random
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr
import pickle
import time
from datetime import timedelta
import sys
import re
import os

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn import metrics

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics.pairwise import euclidean_distances
from sk

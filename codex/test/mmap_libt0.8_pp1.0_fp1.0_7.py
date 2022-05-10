import mmap
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift

from sklearn.cluster import estimate_bandwidth
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AffinityPropagation
from collections import Counter
import statsmodels.api as sm
from statsmodels.tsa.vector_ar.var_model import VAR
import mysql.connector

from numpy import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import io
from gensim.models import KeyedVectors
from nltk.cluster.util import cosine_distance
from sklearn import mixture



import pandas as pd

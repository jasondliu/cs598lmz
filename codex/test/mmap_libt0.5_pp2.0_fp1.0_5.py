import mmap
import numpy as np
import os
import random
import time

from numpy.linalg import norm
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize

import matplotlib.pyplot as plt

from utils import *

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics import euclidean_distances
from sklearn.metrics.pairwise import cosine_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import rbf_kernel

from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans


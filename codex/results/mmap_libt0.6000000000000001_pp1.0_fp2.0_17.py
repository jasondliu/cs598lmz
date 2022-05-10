import mmap
import struct
import math
from itertools import islice
from pathlib import Path
from collections import namedtuple
from collections import Counter
import json
from os import listdir
from os.path import isfile, join
import pickle
import numpy as np
import pandas as pd
import sys
from scipy import sparse
from scipy.sparse import csr_matrix

from sklearn.decomposition import TruncatedSVD
from sklearn.decomposition import NMF
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
from sklearn.metrics import silhouette_score
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import pairwise_distances
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test

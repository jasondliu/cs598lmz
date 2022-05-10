import mmap
import os
import re
import sys
import time

from collections import OrderedDict

import numpy as np

from scipy import stats

from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN

from sklearn.metrics import silhouette_score

from sklearn.preprocessing import StandardScaler

import pandas as pd

from sklearn.metrics import pairwise_distances

import umap

from sklearn.metrics import silhouette_samples

from sklearn.metrics import calinski_harabaz_score

from sklearn.metrics import davies_bouldin_score


def read_data(fname):
   

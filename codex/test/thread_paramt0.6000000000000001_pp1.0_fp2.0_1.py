import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from collections import namedtuple

import numpy as np
import numpy.random as npr

from sklearn.decomposition import PCA

from scipy.spatial import distance
from scipy.linalg import toeplitz

from .utils import *

def _compute_pairwise_distance(X):
    """
    Compute the pairwise distance matrix of the samples in X.
    """
    D = distance.squareform(distance.pdist(X, 'euclidean'))
    D[np.isnan(D)] = 0
    
    return D

def _compute_pairwise_cov(X):
    """
    Compute the pairwise covariance matrix of the samples in X.
    """
    C = np.dot(X, X.T)
    C[np.isnan(C)] = 0
    
    return C


import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from . import utils

import numpy as np
from scipy.spatial.distance import cdist

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

def _get_cluster_centers(embeddings, 
                         n_clusters, 
                         n_init=10, 
                         max_iter=300, 
                         n_jobs=-1):
    """
    Compute cluster centers using KMeans.
    """
    kmeans = KMeans(n_clusters=n_clusters, 
                    n_init=n_init, 
                    max_iter=max_iter, 
                    n_jobs=n_jobs)
    kmeans.fit(embeddings)
    return kmeans.cluster_centers_


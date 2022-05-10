import gc, weakref
from sklearn.metrics.pairwise import euclidean_distances
import sklearn.metrics.pairwise as metrics
from sklearn.neighbors import NearestNeighbors
from sklearn.utils.graph_shortest_path import graph_shortest_path
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import pdb

USE_CYTHON = False

if USE_CYTHON:
    from .cython import (
        cy_augment_neighbors,
        cy_linreg,
        cy_mst,
        cy_mst_approx
    )


class BaseOutlierDetection(BaseEstimator, TransformerMixin):
    """
    Outlier detection base class, wrapping common functions.
    """

    def __init__(self, contamination=0.1, n_neighbors=5, novelty=False,
                 quantile=0.7):
        self.contamination = contamination
        self.n_neighbors

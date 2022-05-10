import gc, weakref

import scipy as sp
from scipy import linalg
from scipy.sparse.linalg import eigsh, eigs
from scipy.sparse import csr_matrix
import numpy as np

from . import (utils, sampling, helpers, graph, regularization,
               decomposition, sparsification, smoothing, quadrature)
from .utils import MODE_CONNECTED, MODE_RAW, MODE_SIMPLE, MODE_ADAPTIVE

__all__ = ["SpectralEmbedding", "SpectralClustering",
           "SpectralBiclustering", "SpectralCoclustering", "LaplacianSpectralEmbedding",
           "weighted_laplacian",
           "get_laplacian", "get_laplacian_matrix", "get_laplacian_embedding",
           "get_lle_embedding",
           "get_hessian_embedding", "get_sde_embedding",
           "get_spectral_embedding", "get

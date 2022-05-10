import gc, weakref
import numpy as np
from numpy import asarray, float32
from numpy.random import randint, rand
from numpy.testing import dec, assert_, assert_raises
from nose.tools import assert_equal, assert_true

from sklearn.utils.testing import assert_greater, assert_less
from sklearn.utils import check_array, check_random_state
from sklearn.utils.extmath import row_norms, safe_sparse_dot
from sklearn.utils.validation import check_is_fitted

from sklearn.cluster import KMeans, MiniBatchKMeans, AffinityPropagation
from sklearn.cluster.k_means_ import _init_centroids, _labels_inertia
from sklearn.cluster.k_means_ import _mini_batch_step, _mini_batch_convergence
from sklearn.cluster.k_means_ import _labels_inertia_minibatch
from sklearn.datasets.samples_generator import make_blobs
from sk

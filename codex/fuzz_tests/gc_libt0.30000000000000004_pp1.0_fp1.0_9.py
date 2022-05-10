import gc, weakref
import numpy as np
import pandas as pd
import scipy.sparse as sps
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize
from sklearn.decomposition import TruncatedSVD
from sklearn.utils.extmath import randomized_svd
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.utils import check_array
from sklearn.utils import check_random_state
from sklearn.utils import gen_even_slices
from sklearn.utils import gen_batches
from sklearn.utils import _get_n_jobs
from sklearn.utils.validation import check_is_fitted
from sklearn.externals.joblib import Parallel
from sklearn.externals.joblib import delayed
from sklearn.externals.joblib import cpu_count
from sklearn.externals.joblib import Memory
from sklearn.externals.joblib import logger
from sklearn.externals.joblib._compat import _basestring
from

import gc, weakref
import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal

from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, dok_matrix, lil_matrix
from scipy.sparse.sputils import isdense, isscalarlike, isintlike
from scipy.sparse.sputils import upcast, upcast_char, upcast_scalar
from scipy.sparse.sputils import getdtype, get_index_dtype
from scipy.sparse.sputils import issequence
from scipy.sparse.sputils import matrix
from scipy.sparse.sputils import ismatrix, isshape
from scipy.sparse.sputils import isintlike, isscalarlike, issequence
from scipy.sparse.sputils import IndexMixin, BlockIndexMixin
from scipy.sparse.sputils import get_sum_dtype, get_

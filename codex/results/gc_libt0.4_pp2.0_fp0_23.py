import gc, weakref
import numpy as np
from numpy.testing import assert_array_equal
from scipy.sparse import csc_matrix
import scipy.sparse.linalg as splinalg
from scipy.sparse.linalg.eigen.arpack import ArpackError
from scipy.sparse.linalg.eigen.arpack.arpack import ArpackNoConvergence
from scipy.sparse.linalg.eigen.arpack.arpack import _arpack
from scipy.sparse.linalg.eigen.arpack.arpack import _ARPACK
from scipy.sparse.linalg.eigen.arpack.arpack import _arpack_wrapper
from scipy.sparse.linalg.eigen.arpack.arpack import _get_funcs
from scipy.sparse.linalg.eigen.arpack.arpack import _get_dtype
from scipy.sparse.linalg.eigen.arpack.arpack import _check_flags

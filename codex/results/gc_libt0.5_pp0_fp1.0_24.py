import gc, weakref
import numpy as np
import numpy.random as nr
from numpy.testing import assert_array_equal

from nose.tools import assert_true, assert_false, assert_equal, assert_raises

from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, dok_matrix, \
        spdiags, bsr_matrix, dia_matrix, lil_matrix, rand
from scipy.sparse import isspmatrix, isspmatrix_csc, isspmatrix_csr, \
        isspmatrix_bsr, isspmatrix_coo, isspmatrix_dok, isspmatrix_lil, \
        isspmatrix_dia

from scipy.sparse.sputils import supported_dtypes, isintlike, issequence
from scipy.sparse.sputils import ismatrix, getdtype, isshape, upcast, \
        upcast_char, upcast_scalar, get_index

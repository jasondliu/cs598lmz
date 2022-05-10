import _struct
import _numpy
from numpy.testing import assert_equal
from numpy.testing.utils import assert_almost_equal, assert_raises

from scipy.sparse import (bsr_matrix, csc_matrix, csr_matrix, dia_matrix,
                          dok_matrix, lil_matrix, rand)

from scipy.sparse.sputils import array_equal, isintlike
from scipy.sparse.sputils import isscalarlike, isshape
from scipy.sparse.sputils import get_index_dtype
from scipy.sparse.sputils import get_dtype
from scipy.sparse.sputils import upcast
from scipy.sparse.sputils import upcast_char
from scipy.sparse.sputils import get_sum_dtype
from scipy.sparse.sputils import get_maxmin_dtype
from scipy.sparse.sputils import issequence
from scipy.

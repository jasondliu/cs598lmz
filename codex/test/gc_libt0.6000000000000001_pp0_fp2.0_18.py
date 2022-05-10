import gc, weakref
import numpy as np
from numpy.testing import (assert_, assert_array_equal, assert_equal,
                           assert_raises, assert_allclose)
import scipy.sparse as sparse
from scipy.sparse.linalg import LinearOperator

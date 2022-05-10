import gc, weakref
import numpy as np
from numpy.testing import (assert_, assert_array_equal, assert_equal,
                           assert_raises, assert_allclose)
import scipy.sparse as sparse
from scipy.sparse.linalg import LinearOperator
from scipy.sparse.linalg.eigen.arpack import eigs
from scipy.sparse.linalg.eigen.arpack.arpack import ArpackNoConvergence
from scipy.sparse.linalg.eigen.arpack.arpack import ArpackError
from scipy.sparse.linalg.eigen.arpack.arpack import ArpackSingularOperator
from scipy.sparse.linalg.eigen.arpack.arpack import ArpackLinearOperatorError
from scipy.sparse.linalg.eigen.arpack.arpack import ArpackDomainError
from scipy.sparse.linalg.eigen.arpack.arpack import _ARPACK

from scipy.

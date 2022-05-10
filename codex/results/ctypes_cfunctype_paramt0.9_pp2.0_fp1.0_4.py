import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

import numpy
from numpy import array, append, arange, sum
from numpy import succesor as succ
from numpy import concatenate, ones, float32
from numpy.linalg import norm

from scipy import weave
from scipy.weave import converters

from tools.general import valuesort

from pysparse import spmatrix
from pysparse import itsolvers
from pysparse import precon
from pysparse import jdsym
from pysparse import precon

from pyamg import relax
from pyamg.classical import ruge_stuben_solver
from pyamg.util.linalg import norm as linalg_norm
from pyamg.util.utils import kron_A_I, kron_I_B
from pyamg.util.utils import get_diagonal, diag_sparse
from pyamg.util.utils import strength_of_connection
from pyamg.util.utils import separate_block
from pyamg.gallery import poisson
from pyamg.rel

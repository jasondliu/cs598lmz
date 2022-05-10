import types
types.ModuleType.__repr__ = lambda self: self.__name__

import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

from pyamg.gallery import stencil_grid
from pyamg.gallery.stencil import poisson
from pyamg.relaxation.smoothing import change_smoothers
from pyamg.util.linalg import norm
from pyamg.util.utils import diag_sparse

from numpy.testing import TestCase, assert_equal, assert_almost_equal, assert_array_almost_equal, assert_array_equal, assert_raises, assert_, run_module_suite


import types
types.ModuleType.__repr__ = lambda self: self.__name__

# We have to do this to avoid a circular import.
import numpy as np
from numpy.testing import (assert_allclose, assert_equal, assert_almost_equal,
                           assert_array_almost_equal, assert_array_equal)


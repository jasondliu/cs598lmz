import types
# Test types.FunctionType doesn't get messed up by this module.
from types import FunctionType

from numpy import testing
from numpy.testing import assert_, assert_array_equal, assert_equal
from numpy import array, asarray
from numpy.random import random, randint, uniform, exponential
from scipy.interpolate.fitpack import dblint
import os
from scipy._lib._version import NumpyVersion
from scipy.interpolate.interpolate import _Interpolator1DWithDerivatives
from scipy.integrate._test_multivariate import FuncData


class Mixin(object):
    # We inherit from object to get new-style classes even with python < 2.2

    _tol = 1e-10

    def test_only_one_routine(self):
        f = dblint.not_implemented_f
        x = self.x
        y = self.y
        self.assertRaises(ValueError, self.spline.set_smoothing_factor, .75)
        self.assertRaises(Value

import codecs
codecs.register_error('surrogateescape', codecs.surrogateescape_error)

import os

import numpy as np
from numpy.testing import dec, assert_, assert_raises,\
    assert_almost_equal, np_errstate, assert_equal, assert_array_equal
from scipy.misc import factorial, comb
from scipy._lib._numpy_compat import suppress_warnings


DECIMAL = 6


class TestFactorial(object):

    def test_basic(self):
        assert_equal(factorial(0), 1)
        assert_equal(factorial(1), 1)
        assert_equal(factorial(10), 3628800)

    def test_negative(self):
        assert_raises(ValueError, factorial, -1)
        assert_raises(ValueError, factorial, -10)

    def test_values(self):
        with np_errstate(over="ignore"):
            # This can overflow, so ignore overflow errors.
            assert_equal(factorial(171),
                         0x5e3

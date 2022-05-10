import io
# Test io.RawIOBase to see if it is a file-like object
# (has a read() method)
#

try:
    f = io.RawIOBase()
    f.read()
except:
    io.RawIOBase = io.IOBase

from numpy import __version__ as numpy_version
from scipy import __version__ as scipy_version
from matplotlib import __version__ as matplotlib_version
from nose import run, SkipTest
from numpy.testing import assert_, assert_equal, assert_almost_equal, \
    assert_array_equal, assert_array_almost_equal, assert_raises, dec, \
    assert_allclose, assert_array_max_ulp, assert_warns, assert_string_equal, \
    assert_no_warnings
import numpy as np
from scipy._lib._util import _asarray_validated
import os
from os.path import abspath, dirname, join
import warnings
import pytest

from scipy import misc
from scipy._lib._numpy_compat import

import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import os
import sys
import warnings

# SOURCE LINE 7

import numpy as np

# SOURCE LINE 9

from numpy.testing import assert_equal, assert_array_equal, assert_array_almost_equal, assert_almost_equal, assert_approx_equal, assert_, assert_raises, dec, TestCase, run_module_suite, assert_allclose, assert_array_less, assert_string_equal, assert_no_warnings

# SOURCE LINE 12

from numpy.testing.utils import *

# SOURCE LINE 14

from numpy.testing.nosetester import NoseTester as Tester
test = Tester().test
bench = Tester().bench

# SOURCE LINE 17

from numpy.testing.noseclasses import KnownFailureTest

# SOURCE LINE 19

from numpy.testing.noseclasses import KnownFailureDidNotFailTest

# SOURCE LINE 21

from numpy.testing.noseclasses import SkipTest


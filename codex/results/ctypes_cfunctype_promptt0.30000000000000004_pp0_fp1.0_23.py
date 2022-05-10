import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE.

# The test function is a simple function that returns the sum of its
# arguments.  It is called with a variety of argument types and the
# results are compared to the results of calling the function directly.

# The test function is defined in a C file and compiled into a shared
# library.  The shared library is loaded using ctypes.CDLL.  The
# function is then called using ctypes.CFUNCTYPE.

# The test function is defined in a C file and compiled into a shared
# library.  The shared library is loaded using ctypes.CDLL.  The
# function is then called using ctypes.CFUNCTYPE.

import os
import unittest
from ctypes import *

class CFuncPtrTest(unittest.TestCase):
    def setUp(self):
        self.libc = CDLL(os.path.join(os.path.dirname(__file__), "ctypes_test.dll"))

    def test_sum(self):
        self.libc

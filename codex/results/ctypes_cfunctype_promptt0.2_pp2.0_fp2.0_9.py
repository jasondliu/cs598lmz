import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the example from the ctypes documentation:
# http://docs.python.org/library/ctypes.html#function-prototypes

import unittest
from test import support

# The following function is used in the test.
# It is defined here so that it can be used both by the test and
# by the code that sets up the argtypes and restype attributes.
def func(i):
    return i + 1

class CFunctionTypeTestCase(unittest.TestCase):

    def test_CFUNCTYPE(self):
        # This is the example from the ctypes documentation.
        # http://docs.python.org/library/ctypes.html#function-prototypes
        from ctypes import c_int, CFUNCTYPE
        prototype = CFUNCTYPE(c_int, c_int)
        paramflags = (1, "i")
        restype = c_int
        func.argtypes = [c_int]
        func.restype = c_int
        f = prototype(("func", __name

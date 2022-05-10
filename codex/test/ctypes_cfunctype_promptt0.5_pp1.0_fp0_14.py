import ctypes
# Test ctypes.CFUNCTYPE.

import ctypes
from ctypes import *

try:
    from ctypes.wintypes import *
except ImportError:
    pass

import unittest

class CFuncPtrTest(unittest.TestCase):
    def test_callbacks(self):
        # callbacks
        restype = c_int
        argtypes = (c_int, c_int)

        def func(*args):
            return args[0] + args[1]

        CMPFUNC = CFUNCTYPE(restype, *argtypes)
        self.failUnlessEqual(CMPFUNC(func)(1, 2), 3)

        # callbacks with out params
        restype = c_int
        argtypes = (c_int, POINTER(c_int))

        def func(*args):
            args[1][0] = args[0] + 1
            return args[0] + 1

        CMPFUNC = CFUNCTYPE(restype, *argtypes)
        a = c_int(0)
        self.failUnlessE

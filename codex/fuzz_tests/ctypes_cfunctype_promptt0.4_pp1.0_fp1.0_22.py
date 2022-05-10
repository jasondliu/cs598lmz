import ctypes
# Test ctypes.CFUNCTYPE

# This test is used to test the CFUNCTYPE type.

from ctypes import *
import unittest

class CFuncPtrTestCase(unittest.TestCase):

    def test_callbacks(self):
        # Check calling a callback function
        restype = c_int
        argtypes = (c_int, c_int)
        def func(*args):
            return args[0] + args[1]
        cfunc = CFUNCTYPE(restype, *argtypes)(func)
        self.failUnlessEqual(cfunc(1, 2), 3)

        # Check calling a callback function with keyword arguments
        restype = c_int
        argtypes = (c_int, c_int)
        def func(a, b):
            return a + b
        cfunc = CFUNCTYPE(restype, *argtypes)(func)
        self.failUnlessEqual(cfunc(b=2, a=1), 3)

        # Check calling a callback function with wrong number of arguments
        restype = c_int
       

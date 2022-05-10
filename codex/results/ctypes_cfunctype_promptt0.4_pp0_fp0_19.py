import ctypes
# Test ctypes.CFUNCTYPE

# This test is a bit special, because it doesn't really test the
# library, but the ctypes module itself.

# The CFUNCTYPE class is used as a base class for the rest of the
# ctypes classes.  It implements the __call__ method, which is used
# to call the function.

import unittest
from ctypes import *
from ctypes.test import is_resource_enabled

class CFUNCTYPETestCase(unittest.TestCase):
    def test_call_1(self):
        # calling a function with a simple result
        # (no arguments, integer result)
        dll = CDLL(ctypes.util.find_library("c"))
        func = CFUNCTYPE(c_int, c_int)(("abs", dll), ((1, "j"),))
        self.failUnlessEqual(func(1), 1)
        self.failUnlessEqual(func(-1), 1)

    def test_call_2(self):
        # calling a function with a simple result
        # (no arguments,

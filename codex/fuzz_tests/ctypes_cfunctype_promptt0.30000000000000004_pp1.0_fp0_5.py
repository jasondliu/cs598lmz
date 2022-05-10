import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a test case for http://bugs.python.org/issue1202.
#
# The problem was that the CFUNCTYPE() constructor did not properly
# initialize the c_functype_cache dictionary.  This caused a crash
# when the CFUNCTYPE() constructor was called recursively from within
# a callback function.

import unittest
from test import test_support

class CFUNCTYPETestCase(unittest.TestCase):
    def test_recursive_call(self):
        # This function calls CFUNCTYPE() recursively.
        def func(n):
            if n <= 0:
                return 0
            else:
                # This is the recursive call.
                cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
                return cb(n-1) + 1

        # This function calls func() and checks the result.
        def test(n):
            cb = ctypes.CFUNCTYPE(ctypes.c_int

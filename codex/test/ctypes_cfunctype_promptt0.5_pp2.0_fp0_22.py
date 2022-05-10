import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a test for ctypes.CFUNCTYPE, a function which creates a
# ctypes function prototype, which can be used to call C functions.
#
# The test will fail if the ctypes.CFUNCTYPE function is not implemented
# correctly.

import unittest
from ctypes import *

class CFUNCTYPETestCase(unittest.TestCase):

    def test_basic(self):
        # Simple function
        func = CFUNCTYPE(c_int, c_int)(lambda x: x)
        self.assertEqual(func(42), 42)

    def test_integer_arg(self):
        # Test various integer argument types
        func = CFUNCTYPE(c_int, c_int)(lambda x: x)
        self.assertEqual(func(42), 42)
        func = CFUNCTYPE(c_int, c_long)(lambda x: x)
        self.assertEqual(func(42), 42)

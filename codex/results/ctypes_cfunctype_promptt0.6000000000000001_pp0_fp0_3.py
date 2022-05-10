import ctypes
# Test ctypes.CFUNCTYPE() with a callback that takes an array of floats.
#
# This test is based on ctypes/test/test_callback.py by Thomas Heller.

import unittest
from ctypes import *

class ArrayTest(unittest.TestCase):
    def test_array(self):
        from _ctypes import Array

        # The following callback function is called from the dll.
        # It sums up the values in the array, and returns the result.
        # The result is compared to the expected value.
        # The array type is specified by argtypes, so the callback
        # function must use a ctypes array type to get the correct result.
        def func(values):
            sum = 0
            for v in values:
                sum = sum + v
            return sum

        f = CFUNCTYPE(c_int, POINTER(c_float))(func)
        self.assertEqual(f((c_float*4)(1, 2, 3, 4)), 10)
        self.assertEqual(f((c_float*1)(42)), 42)

        f =

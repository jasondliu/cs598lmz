import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of the ctypes.CFUNCTYPE function.
# This function is used to create C callback functions.
#
# The test is a simple example of using a callback function
# to sort an array of integers.
#
# The example is from the Python documentation.

from ctypes import *
import unittest

class CFuncPtrTest(unittest.TestCase):
    def test_CFuncPtr(self):
        # Prototype a comparison function
        CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

        # Define a helper function to compare two elements
        # Function matches the CMPFUNC prototype
        def py_cmp_func(a, b):
            return a[0] - b[0]

        # Convert the Python comparison function into a C pointer
        cmp_func = CMPFUNC(py_cmp_func)

        # Define an array of C ints
        array_type = c_int * 5
        values = array_type(5, 4,

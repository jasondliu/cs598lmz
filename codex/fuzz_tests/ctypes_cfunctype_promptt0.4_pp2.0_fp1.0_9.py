import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is used to check the ctypes.CFUNCTYPE() function.
#
# The test is based on the fact that the ctypes.CFUNCTYPE() function
# returns a callable object that can be used to call the function.
#
# The test checks that the function is called and that the function
# returns a value.
#

import unittest
from test import support

#
# The function to be called by the ctypes.CFUNCTYPE() function.
#
def func(a, b):
    return a + b

#
# The test case
#
class CFunctionTypeTestCase(unittest.TestCase):
    def test_CFUNCTYPE(self):
        #
        # Create a ctypes.CFUNCTYPE() function object.
        #
        cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
        #
        # Call the function object.
        #
        result = cfunc(func)(1

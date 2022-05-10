import ctypes
# Test ctypes.CFUNCTYPE()
#
# This test is derived from the ctypes tutorial, and is used to test
# the ctypes.CFUNCTYPE() function.
#
# http://docs.python.org/library/ctypes.html#function-prototypes

import unittest
from test import test_support

import ctypes

class CFuncPtrTestCase(unittest.TestCase):

    def test_CFUNCTYPE(self):
        # CFUNCTYPE() creates a prototype for a C function.
        # The first argument is the return type, the rest are the argument types.
        #
        # The prototype can be called like a Python function, and the
        # arguments to the Python function are converted to the appropriate
        # C data types.
        #
        # The prototype can also be called like a C function, and the
        # Python result is converted to the return type of the prototype.

        # Create a prototype for a function with a double argument, and no
        # return value.
        prototype = ctypes.CFUNCTYPE(None, ctypes.c_double)

import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit different from the others, because it doesn't
# use the test_support framework.  It is run by Lib/test/test_ctypes.py.

import unittest
from ctypes import *

class CFuncPtrTestCase(unittest.TestCase):

    def test_callbacks(self):
        # Test calling a callback function
        #
        # The callback function is called with a pointer to a C int,
        # and should set the int to 42.
        #
        # The callback is called from a C helper function, which is
        # called from Python.
        #
        # The C helper function is passed a pointer to a Python object,
        # which is used to keep the Python callback alive.  This is
        # necessary because the C helper function is called from C code
        # which doesn't know anything about Python.
        #
        # The C helper function is also passed a pointer to a C int,
        # which is used to communicate the result back to Python.
        #
        # The C helper function is also passed a pointer to the

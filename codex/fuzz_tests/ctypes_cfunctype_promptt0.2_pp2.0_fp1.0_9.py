import ctypes
# Test ctypes.CFUNCTYPE()

# This test is a bit tricky, because it has to work on both Python 2 and 3.
# On Python 2, the ctypes module is written in Python, and the CFUNCTYPE()
# function is implemented in Python.  On Python 3, the ctypes module is
# written in C, and the CFUNCTYPE() function is implemented in C.
#
# The Python 2 implementation of CFUNCTYPE() is not very robust, and
# doesn't handle all the cases that the C implementation does.  So we
# have to be careful to test only cases that work on both Python 2 and 3.

import sys
import unittest
from test import support

class CFunctionTypeTestCase(unittest.TestCase):
    def test_basic(self):
        # Check that we can create a CFUNCTYPE() instance.
        # This is a bit tricky, because the instance has no __name__
        # attribute, so we can't use isinstance() to check its type.
        # Instead, we check the type of its __call__ method.
        f = ctypes.

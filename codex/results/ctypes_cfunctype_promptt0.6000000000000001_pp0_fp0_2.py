import ctypes
# Test ctypes.CFUNCTYPE
#
import unittest
from ctypes import *

class CFuncPtrTest(unittest.TestCase):
    def test_prototype(self):
        # This test fails with Python 2.3, 2.4, 2.5 and 2.6.
        # Only 2.7 and 3.1 are fine.
        #
        # This is a bug in Python: the type of the function object returned
        # by CFUNCTYPE() is not a Python function type.  It's a C function
        # pointer type.
        #
        # In Python 2.x, the type() function returns the C function pointer
        # type instead of the Python function type.  In Python 3.x, type()
        # returns the Python function type.
        #
        # This test is here to document this bug.
        #
        # See also:
        #   http://bugs.python.org/issue3290
        #   http://bugs.python.org/issue4967
        #
        # The actual bug is that the type of the function object should be
        # the Python function type,

import ctypes
# Test ctypes.CFUNCTYPE()
#
# This is a test to verify that ctypes.CFUNCTYPE(...) creates a type
# object with a correct __name__ attribute.
#
# More information:
# http://bugs.python.org/issue10726

import unittest
from ctypes import *

class CFUNCTYPETest(unittest.TestCase):
    def test_name(self):
        # Try to create a CFUNCTYPE() instance in a few different ways.
        # The resulting type object should have a __name__ attribute.
        #
        # Note: The __name__ attribute is not documented.  It is used
        # by the inspect module.
        #
        # Note: The __name__ attribute is not required by any PEP.
        # It is a useful convenience feature for developers.
        for name in ["foo", "bar", "baz", "quux"]:
            for restype, argtypes in [
                    (c_int, ()),
                    (c_int, (c_int,)),
                    (c_int, (c_int,

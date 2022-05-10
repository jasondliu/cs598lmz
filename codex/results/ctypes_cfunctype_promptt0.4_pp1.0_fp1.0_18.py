import ctypes
# Test ctypes.CFUNCTYPE
#
# The following tests are based on the test_cfunctype.py test suite
# from CPython 3.2.

from ctypes import *

import unittest
from test import support
from ctypes import _testcapi

class CFuncPtrTestCase(unittest.TestCase):

    def test_simple(self):
        # Simple test for CFUNCTYPE, check that the argtypes tuple
        # is correctly set.
        f = CFUNCTYPE(c_int, c_int, c_int)
        self.assertEqual(f.argtypes, (c_int, c_int))

    def test_argtypes_readonly(self):
        # Check that the argtypes attribute is readonly.
        f = CFUNCTYPE(c_int, c_int, c_int)
        self.assertRaises(TypeError, setattr, f, "argtypes", (c_int,))

    def test_restype_readonly(self):
        # Check that the restype attribute is readonly.
        f =

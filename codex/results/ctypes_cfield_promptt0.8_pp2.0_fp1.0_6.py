import ctypes
# Test ctypes.CField and ctypes.CFuncPtr objects

from ctypes import *
import unittest
from test import support

import _ctypes_test

class CFieldTestCase(unittest.TestCase):
    def test_c_int_restype(self):
        # Bug 1018: ctypes.c_int.restype is overwritten at runtime
        # and ctypes.c_int.restype is the same as c_int_p.restype
        self.assertIs(c_int.restype, c_int_p.restype)

        INT_MAX = 2 ** (sizeof(c_int) * 8 - 1) - 1
        c_int.restype = c_int

        class X(Structure):
            _fields_ = [("value", c_int)]

        lib = CDLL(_ctypes_test.__file__)
        lib.c_int_func.restype = c_int
        lib.c_int_func.argtypes = [c_int]

        self.assertEqual(X.value.__get__(X(

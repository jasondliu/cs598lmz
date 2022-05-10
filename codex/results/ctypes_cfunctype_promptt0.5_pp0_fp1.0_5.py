import ctypes
# Test ctypes.CFUNCTYPE

import unittest
from test import support
import _ctypes_test
dll = _ctypes_test.dll

class CFuncPtrTestCase(unittest.TestCase):
    def test_restype_none(self):
        # restype None: the function returns None
        f = dll._testfunc_p_p
        f.restype = None
        self.assertEqual(f(b"foo"), None)
        self.assertEqual(f(42), None)

    def test_restype_int(self):
        # restype int: the function returns an integer
        f = dll._testfunc_p_p
        f.restype = ctypes.c_int
        self.assertEqual(f(b"foo"), 3)
        self.assertEqual(f(42), 2)

    def test_restype_float(self):
        # restype float: the function returns a float
        f = dll._testfunc_p_p
        f.restype = ctypes.c_float
        self.assertEqual

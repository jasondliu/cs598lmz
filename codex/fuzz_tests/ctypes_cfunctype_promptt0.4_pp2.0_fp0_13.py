import ctypes
# Test ctypes.CFUNCTYPE

import sys
import unittest
from test import support

libc = ctypes.CDLL(support.findfile("_ctypes_test.so"))

class CFunctionTypeTestCase(unittest.TestCase):
    def test_restype_none(self):
        # c_int() returns 0, c_int(42) returns 42
        func = ctypes.CFUNCTYPE(None, ctypes.c_int)
        self.assertEqual(func(), None)
        self.assertEqual(func(42), None)

    def test_restype_int(self):
        # c_int() returns 0, c_int(42) returns 42
        func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        self.assertEqual(func(), 0)
        self.assertEqual(func(42), 42)

    def test_restype_float(self):
        # c_float() returns 0.0, c_float(42) returns 42.0
        func = ctypes

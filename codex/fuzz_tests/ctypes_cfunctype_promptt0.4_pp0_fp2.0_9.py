import ctypes
# Test ctypes.CFUNCTYPE

import sys
import unittest
from test import support

class CFunctionTypeTestCase(unittest.TestCase):

    def test_basic(self):
        # Basic test of CFUNCTYPE()
        f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        self.assertEqual(f(42), 42)

    def test_restype_none(self):
        # CFUNCTYPE(None, ...) is allowed
        ctypes.CFUNCTYPE(None, ctypes.c_int)

    def test_argtypes_none(self):
        # CFUNCTYPE(..., None) is allowed
        ctypes.CFUNCTYPE(ctypes.c_int, None)

    def test_argtypes_tuple(self):
        # CFUNCTYPE(..., (..., ...)) is allowed
        ctypes.CFUNCTYPE(ctypes.c_int, (ctypes.c_int, ctypes.c_int))

    def test_

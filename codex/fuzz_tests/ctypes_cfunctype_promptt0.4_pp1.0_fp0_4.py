import ctypes
# Test ctypes.CFUNCTYPE.

import unittest
from test import test_support

class CFuncTypeTestCase(unittest.TestCase):

    def test_basic(self):
        # simple function
        func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x+1)
        self.assertEqual(func(41), 42)

    def test_restype_none(self):
        # function with None as restype
        func = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)
        self.assertEqual(func(41), None)

    def test_restype_void(self):
        # function with None as restype
        func = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)
        self.assertEqual(func(41), None)

    def test_errcheck(self):
        # function with None as restype
        func = ctypes.CFUNCTYPE(None, ctypes.c_

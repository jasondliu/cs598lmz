import ctypes
# Test ctypes.CFUNCTYPE

import unittest
from test import support

class CFuncPtrTest(unittest.TestCase):

    def test_basic(self):
        # Simple test to check that CFUNCTYPE works at all
        f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 42)
        self.assertEqual(f(8), 50)

    def test_errcheck(self):
        # Check that errcheck is called
        def errcheck(result, func, arguments):
            return arguments[0] * 2
        f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 42,
                                                          errcheck=errcheck)
        self.assertEqual(f(8), 16)

    def test_restype(self):
        # Check that restype is called
        def restype(value, func, arguments):
            return value * 2
        f = ctypes.CFUNCTYPE(ctypes.c_int,

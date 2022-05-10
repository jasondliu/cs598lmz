import ctypes
# Test ctypes.CFUNCTYPE

import sys
import unittest

from test import support

@unittest.skipUnless(hasattr(ctypes, 'CFUNCTYPE'), 'requires CFUNCTYPE')
class CFuncPtrTestCase(unittest.TestCase):

    def test_argtypes(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.assertRaises(TypeError, CFuncPtr, X)

    def test_restype(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.assertRaises(TypeError, CFuncPtr, X)

    def test_call_integer_return(self

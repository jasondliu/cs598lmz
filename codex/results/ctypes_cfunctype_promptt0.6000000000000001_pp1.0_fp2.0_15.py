import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *
import unittest


class CFUNCTYPETestCase(unittest.TestCase):

    def test_argtypes(self):
        from _ctypes import ArgumentError
        self.assertRaises(TypeError, CFUNCTYPE, None)
        self.assertRaises(TypeError, CFUNCTYPE, 42)
        self.assertRaises(TypeError, CFUNCTYPE, "spam")
        self.assertRaises(ArgumentError, CFUNCTYPE, c_int, c_int)

    def test_errcheck(self):
        from _ctypes import ArgumentError
        self.assertRaises(TypeError, CFUNCTYPE, c_int, errcheck=None)
        self.assertRaises(TypeError, CFUNCTYPE, c_int, errcheck=42)
        self.assertRaises(TypeError, CFUNCTYPE, c_int, errcheck="spam")
        self.assertRaises(ArgumentError, CFUNCTYPE, c_int, err

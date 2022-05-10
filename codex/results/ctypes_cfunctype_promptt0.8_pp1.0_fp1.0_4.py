import ctypes
# Test ctypes.CFUNCTYPE instantiation with different number of parameters.
from ctypes import *
import unittest
import _ctypes_test

# from _ctypes_test import func, func_si
func = _ctypes_test.func
func_si = _ctypes_test.func_si

class CFuncPtrTestCase(unittest.TestCase):

    def setUp(self):
        self.f = CFUNCTYPE(c_int, c_int)
        self.g = CFUNCTYPE(c_int, c_int, c_int)
        self.h = CFUNCTYPE(c_int, c_int, c_int, c_int)
        self.i = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int)

    def test_argtypes(self):
        self.assertEqual(self.f.argtypes, (c_int,))
        self.assertEqual(self.g.argtypes, (c_int, c_int))
        self.assertEqual

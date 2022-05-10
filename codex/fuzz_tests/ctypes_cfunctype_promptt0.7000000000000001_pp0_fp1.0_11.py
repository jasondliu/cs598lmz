import ctypes
# Test ctypes.CFUNCTYPE(), ctypes.POINTER(), and ctypes.byref()
from ctypes import *
from ctypes.test import needs_smp
import unittest, sys


@needs_smp
class PointerTest(unittest.TestCase):
    def setUp(self):
        self.functype = CFUNCTYPE(c_int, c_int)

    def test_basic(self):
        f = self.functype(lambda x: 2 * x)
        self.assertEqual(f(41), 82)
        self.assertEqual(f(42), 84)
        self.assertIs(f.restype, c_int)
        self.assertEqual(f.argtypes, [c_int])

    def test_byref(self):
        f = self.functype(lambda x: 2 * x)
        x = c_int(41)
        self.assertEqual(f(byref(x)), 82)
        self.assertEqual(f(byref(x)), 82)
        self.assertEqual(

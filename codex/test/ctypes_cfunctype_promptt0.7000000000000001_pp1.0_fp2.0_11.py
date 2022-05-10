import ctypes
# Test ctypes.CFUNCTYPE (Issue #3495)
from ctypes import *
import unittest

class CFuncPtrTest(unittest.TestCase):

    def test_simple(self):
        func = CFUNCTYPE(c_int, c_int, c_int)(lambda x, y: x + y)
        self.assertEqual(func(2, 3), 5)

    def test_restype(self):
        func = CFUNCTYPE(c_float)(lambda x: float(x))
        self.assertEqual(func(2), 2.0)

    def test_argtypes(self):
        func = CFUNCTYPE(None, c_int, c_int)(lambda x, y: None)
        self.assertEqual(func.argtypes, [c_int, c_int])

    def test_callbacks(self):
        func = CFUNCTYPE(None, c_int, c_int)
        def callback(x, y):
            callback.called = True
            self.assertEqual(x, 2)
            self

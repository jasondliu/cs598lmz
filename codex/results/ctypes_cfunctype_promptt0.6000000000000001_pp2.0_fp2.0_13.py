import ctypes
# Test ctypes.CFUNCTYPE when a function has a bool return type
# and a bool argument.
from ctypes import *
import unittest

class BoolTestCase(unittest.TestCase):
    def test_bool(self):
        BOOL = c_int
        LPBOOL = POINTER(BOOL)

        @CFUNCTYPE(BOOL, BOOL)
        def func(arg):
            return arg

        p = func(True)
        self.assertEqual(p, True)
        p = func(False)
        self.assertEqual(p, False)

        p = func(1)
        self.assertEqual(p, True)
        p = func(0)
        self.assertEqual(p, False)

        p = func(1.0)
        self.assertEqual(p, True)
        p = func(0.0)
        self.assertEqual(p, False)

        p = func(1L)
        self.assertEqual(p, True)
        p = func(0L)
        self.assert

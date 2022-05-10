import ctypes
# Test ctypes.CFUNCTYPE

# This test is based on a test originally written by Martin v. Löwis,
# and placed in the public domain.

import unittest
from test import support
from ctypes import *

class Callbacks(unittest.TestCase):
    def test_0(self):
        self.assertRaises(TypeError, CFUNCTYPE(c_int))
        self.assertRaises(TypeError, CFUNCTYPE(c_int), lambda x: x)

    def test_1(self):
        POINTER(c_int)
        prototype = CFUNCTYPE(POINTER(c_int), c_int)
        paramflags = (1, "x")
        def func(*args):
            self.assertEqual(args, paramflags)
            return args
        cfunc = prototype(func, paramflags)
        self.assertEqual(cfunc.argtypes, (c_int,))
        self.assertEqual(cfunc.restype, POINTER(c_int))
        self.assertEqual(cfunc(42

import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *
from ctypes.test import need_symbol

import unittest
from test import test_support

class CFuncPtrTestCase(unittest.TestCase):

    def test_simple(self):
        prototype = CFUNCTYPE(c_int, c_int, c_int)
        paramflags = (1, "x", 0), (1, "y", 0)
        cfunc = prototype((b"xy", paramflags), ((1, "return x+y"),))

        self.assertEqual(cfunc(2, 3), 5)
        self.assertEqual(cfunc(2, -3), -1)

    def test_simple_with_struct(self):
        class X(Structure):
            _fields_ = [("a", c_int)]

        prototype = CFUNCTYPE(c_int, POINTER(X))
        paramflags = (1, "x", 0),
        cfunc = prototype((b"x", paramflags), ((1, "return x.contents.a"),))

       

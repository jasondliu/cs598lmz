import ctypes
# Test ctypes.CField.

# This file is part of the ctypes tests.

import unittest
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int)]

class Y(Structure):
    _fields_ = [("x", X)]

class Z(Structure):
    _fields_ = [("y", Y)]

class Test(unittest.TestCase):
    def test_field(self):
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(Y.x.offset, 0)
        self.assertEqual(Z.y.offset, 0)

        self.assertEqual(X.a.size, sizeof(c_int))
        self.assertEqual(Y.x.size, sizeof(X))
        self.assertEqual(Z.y.size, sizeof(Y))

        self.assertEqual(X.a.index, 0)
        self.assertEqual(Y.x.index, 0)
        self.assertEqual(Z.y

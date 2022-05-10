import ctypes
# Test ctypes.CField.from_address

import unittest
from test import support

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

class Test(unittest.TestCase):
    def test_simple(self):
        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual(x.b, 0)

        x.a = 42
        x.b = -99

        self.assertEqual(x.a, 42)
        self.assertEqual(x.b, -99)

    def test_from_address(self):
        x = X()
        y = Y()
        z = Z()

        self

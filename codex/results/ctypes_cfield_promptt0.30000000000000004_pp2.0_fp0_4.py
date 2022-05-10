import ctypes
# Test ctypes.CField.from_address()

import unittest
from test import test_support

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", Y)]

class FromAddressTestCase(unittest.TestCase):
    def test_from_address(self):
        z = Z()
        self.assertEqual(ctypes.c_int.from_address(ctypes.addressof(z.x)).value, 0)
        self.assertEqual(ctypes.c_int.from_address(ctypes.addressof(z.y)).value, 0)

        z.x.a = 42
        z.y.b = 99
        self.assertEqual(ctypes.c_int.from_address(ctypes.addressof(z.x)).value, 42)

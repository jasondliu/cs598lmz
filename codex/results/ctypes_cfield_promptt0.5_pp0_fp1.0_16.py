import ctypes
# Test ctypes.CField.from_address
from ctypes import *
import unittest
from test import support

class X(Structure):
    _fields_ = [("value", c_int)]

class Y(Structure):
    _fields_ = [("x", X)]

class Z(Structure):
    _fields_ = [("y", Y),
                ("name", c_char_p)]

class FromAddressTestCase(unittest.TestCase):
    def test_from_address(self):
        x = X()
        x.value = 42
        p = pointer(x)
        y = Y.from_address(p.value)
        self.assertEqual(y.x.value, 42)
        z = Z.from_address(p.value)
        self.assertEqual(z.y.x.value, 42)

    def test_from_address_raises(self):
        x = X()
        x.value = 42
        p = pointer(x)
        self.assertRaises(ValueError, Z.from_address, p.

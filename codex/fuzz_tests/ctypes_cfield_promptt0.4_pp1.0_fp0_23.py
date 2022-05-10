import ctypes
# Test ctypes.CField.
import unittest
from test import support

class CFieldTest(unittest.TestCase):

    def test_int_field(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        x = X()
        self.assertEqual(x.a, 0)
        x.a = 42
        self.assertEqual(x.a, 42)
        self.assertRaises(TypeError, setattr, x, "a", "hello")
        self.assertRaises(TypeError, setattr, x, "a", 1.0)
        self.assertRaises(TypeError, setattr, x, "a", (1, 2))
        self.assertRaises(TypeError, setattr, x, "a", [1, 2])

    def test_float_field(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_float)]
        x = X()
        self.assertEqual(x.a, 0

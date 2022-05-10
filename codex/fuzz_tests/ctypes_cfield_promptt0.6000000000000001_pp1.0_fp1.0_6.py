import ctypes
# Test ctypes.CField.

import array
import unittest

from test.test_support import run_unittest

class TestCField(unittest.TestCase):
    def test_set_attribute(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]

        x = X()
        x.a = 2
        self.assertEqual(x.a, 2)

        x.b = 3
        self.assertEqual(x.b, 3)

        self.assertRaises(AttributeError, setattr, x, "c", 4)

    def test_set_item(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        x = X()
        x["a"] = 2
        self.assertEqual(x.a, 2)

        x["b"] = 3
        self.assertEqual(x.b

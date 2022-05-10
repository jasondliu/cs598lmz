import ctypes
# Test ctypes.CField

import ctypes
import unittest

class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]

        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual(x.b, 0)

        x.a = 42
        self.assertEqual(x.a, 42)
        self.assertEqual(x.b, 0)

        x.b = -1
        self.assertEqual(x.a, 42)
        self.assertEqual(x.b, -1)

    def test_array(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int * 4)]

        x = X()
        self.assertEqual(x.a[0], 0)
        self.assertEqual(x.a[1], 0)

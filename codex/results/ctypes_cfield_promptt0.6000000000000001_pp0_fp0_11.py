import ctypes
# Test ctypes.CField.

import unittest


class CFieldTestCase(unittest.TestCase):
    def test_cfld_get(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]

        x = X()
        self.assertEqual(x._a, 0)
        self.assertEqual(x._b, 0)

    def test_cfld_set(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]

        x = X()
        x._a = 1
        x._b = 2
        self.assertEqual(x._a, 1)
        self.assertEqual(x._b, 2)

    def test_cfld_get_nested(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b",

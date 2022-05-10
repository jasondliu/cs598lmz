import ctypes
# Test ctypes.CField.

import unittest
from test import support

class CFieldTestCase(unittest.TestCase):
    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]

        self.assertEqual(ctypes.sizeof(X), 8)


        class Y(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 4),
                        ("c", ctypes.c_int, 4),
                        ("d", ctypes.c_int)]

        self.assertEqual(ctypes.sizeof(Y), 8)

        class Z(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 4),
                        ("c", ctypes.c_int, 4),
                        ("d", ctypes.c_int),
                        ("e", ctypes

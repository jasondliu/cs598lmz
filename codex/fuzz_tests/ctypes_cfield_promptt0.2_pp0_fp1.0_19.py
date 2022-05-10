import ctypes
# Test ctypes.CField.from_address()

import unittest
from test import support

class CFieldTest(unittest.TestCase):
    def test_from_address(self):
        # Test ctypes.CField.from_address()
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]

        x = X()
        x.a = 1
        x.b = 2
        self.assertEqual(ctypes.c_int.from_address(id(x)).value, 1)
        self.assertEqual(ctypes.c_int.from_address(id(x) + ctypes.sizeof(ctypes.c_int)).value, 2)

        class Y(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int)]

        y = Y()
        y.a = 1
        y.b = 2


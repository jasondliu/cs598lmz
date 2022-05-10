import ctypes
# Test ctypes.CField()

import ctypes
import unittest

class TestCField(unittest.TestCase):

    def test_c_field(self):
        class X(ctypes.Structure):
            _fields_ = [
                ("a", ctypes.c_int, 8),
                ("b", ctypes.c_int, 16),
                ("c", ctypes.c_int, 8),
            ]
        x = X()
        self.assertEqual(ctypes.sizeof(x), 4)

    def test_c_field_packed(self):
        class X(ctypes.Structure):
            _fields_ = [
                ("a", ctypes.c_int, 8),
                ("b", ctypes.c_int, 16),
                ("c", ctypes.c_int, 8),
            ]
            _pack_ = 1
        x = X()
        self.assertEqual(ctypes.sizeof(x), 4)

    def test_c_field_packed_2(self):
        class X(ctypes.Structure):

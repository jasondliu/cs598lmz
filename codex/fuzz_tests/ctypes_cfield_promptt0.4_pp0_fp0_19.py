import ctypes
# Test ctypes.CField.

import unittest
from test import support

class CFieldTest(unittest.TestCase):
    def test_field_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char * 4),
                        ("c", ctypes.c_longlong),
                        ("d", ctypes.c_char * 4),
                        ("e", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), 24)
        self.assertEqual(ctypes.sizeof(X._fields_[0][1]), 4)
        self.assertEqual(ctypes.sizeof(X._fields_[1][1]), 4)
        self.assertEqual(ctypes.sizeof(X._fields_[2][1]), 8)
        self.assertEqual(ctypes.sizeof(X._fields_[3][1]), 4)
        self.assertEqual(ctypes.sizeof(X._fields_[4

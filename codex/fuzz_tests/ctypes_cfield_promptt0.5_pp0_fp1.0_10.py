import ctypes
# Test ctypes.CField

import unittest
from test import test_support

class CFieldTest(unittest.TestCase):

    def test_field_sizeof(self):
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(S.x), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(S.x), ctypes.sizeof(ctypes.c_long))
        self.assertEqual(ctypes.sizeof(S.x), ctypes.sizeof(ctypes.c_void_p))
        self.assertEqual(ctypes.sizeof(S.x), ctypes.sizeof(ctypes.c_char_p))
        self.assertEqual(ctypes.sizeof(S.x), ctypes.sizeof(ctypes.c_wchar_p))

        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int

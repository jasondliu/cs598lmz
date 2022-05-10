import ctypes
# Test ctypes.CField.

import ctypes
import unittest

class CFieldTestCase(unittest.TestCase):
    def test_c_field(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        p = POINT(10, 20)
        self.assertEqual(p.x, 10)
        self.assertEqual(p.y, 20)

        p.x = 30
        self.assertEqual(p.x, 30)

        p.y = 40
        self.assertEqual(p.y, 40)

    def test_c_field_with_offset(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("pt", POINT),
                        ("width", ctypes.c_int),
                        ("height

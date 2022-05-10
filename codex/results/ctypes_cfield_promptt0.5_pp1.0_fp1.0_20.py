import ctypes
# Test ctypes.CField.

import unittest
from test import test_support


class CFieldTestCase(unittest.TestCase):
    def test_simple(self):
        # Check a simple field.
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        p = POINT(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_nested(self):
        # Check nested fields.
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("origin", POINT),
                        ("width", ctypes.c_int),
                        ("height", ctypes.c_int)]

        r = RECT(POINT(1, 2), 3, 4)
        self.assert

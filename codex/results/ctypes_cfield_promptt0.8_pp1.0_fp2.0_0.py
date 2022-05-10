import ctypes
# Test ctypes.CField class and related functionality.
import unittest
from test import support

class CFieldTestCase(unittest.TestCase):

    def test_non_struct_field(self):
        # Test ctypes.CField against non-struct classes
        # Issue6293: Crash in ctypes.CField()
        with self.assertRaises(TypeError):
            ctypes.CField()

    def test_field_offset(self):
        class Point(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
        self.assertEqual(Point.x.offset, 0)
        self.assertEqual(Point.y.offset, ctypes.sizeof(ctypes.c_int))

    def test_field_offset_with_gap(self):
        class Point(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("_", ctypes.c_double),
                        ("y", ctypes.c_int)]
        self.assert

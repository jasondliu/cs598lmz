import ctypes
# Test ctypes.CField

# XXX: This is not a full test.  It needs more test cases.

import unittest

class CFieldTest(unittest.TestCase):
    def test_structure_field(self):
        # Testing structure field
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(POINT.y.offset, ctypes.sizeof(ctypes.c_int)*2)

    def test_union_field(self):
        # Testing union field
        class POINT(ctypes.Union):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, 0)

    def test_nested_field

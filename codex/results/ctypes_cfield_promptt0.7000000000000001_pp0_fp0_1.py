import ctypes
# Test ctypes.CField
import unittest

class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class POINT(ctypes.Structure):
            _fields_ = [
                ("x", ctypes.c_long),
                ("y", ctypes.c_long)
            ]
        pt = POINT(10, 20)
        self.assertEqual(pt.x, 10)
        self.assertEqual(pt.y, 20)
        self.assertEqual(ctypes.sizeof(pt), ctypes.sizeof(ctypes.c_long) * 2)
        self.assertEqual(ctypes.addressof(pt.x), ctypes.addressof(pt))

    def test_simple_with_offset(self):
        class POINT(ctypes.Structure):
            _fields_ = [
                ("x", ctypes.c_long),
                ("y", ctypes.c_long, 4)
            ]
        pt = POINT(10, 20)
        self.assertEqual(ctypes.

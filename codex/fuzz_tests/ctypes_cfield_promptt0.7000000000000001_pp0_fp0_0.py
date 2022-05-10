import ctypes
# Test ctypes.CField
import ctypes
import unittest
from ctypes import *

class CFoo(Structure):
    _fields_ = [("x", c_int),
                ("y", c_double)]

class CFieldTest(unittest.TestCase):
    def test_read(self):
        f = CFoo()
        self.assertEqual(sizeof(CFoo), ctypes.sizeof(c_int) + ctypes.sizeof(c_double))
        self.assertEqual(f.x, 0)
        self.assertEqual(f.y, 0.0)

    def test_write(self):
        f = CFoo()
        f.x = 42
        f.y = 3.1415
        self.assertEqual(f.x, 42)
        self.assertEqual(f.y, 3.1415)

    def test_subclass(self):
        # Issue 5: CField objects should be subclassable.
        class CFoo(Structure):
            _fields_ = [("x", c_int),
                        ("

import ctypes
# Test ctypes.CField

import ctypes
import unittest

class CFieldTestCase(unittest.TestCase):
    def test(self):
        class X(ctypes.Structure):
            _fields_ = [
                ('a', ctypes.c_long, 8),
                ('b', ctypes.c_long, 8),
                ('c', ctypes.c_long, 8),
                ('d', ctypes.c_long, 8),
            ]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, 4)
        self.assertEqual(X.a.bitsize, 8)
        self.assertEqual(X.b.offset, 0)
        self.assertEqual(X.b.size, 4)
        self.assertEqual(X.b.bitsize, 8)
        self.assertEqual(X.c.offset, 0)
        self.assertEqual(X.c.size, 4)
        self.assertEqual(X.c.bitsize, 8)

import ctypes
# Test ctypes.CField, ctypes.CFieldP

import unittest
from test import test_support

class CFieldTest(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.LittleEndianStructure):
            _fields_ = [
                ("a", ctypes.c_byte),
                ("b", ctypes.c_byte, 4),
                ("c", ctypes.c_byte, 4),
                ("d", ctypes.c_byte)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, 1)
        self.assertEqual(X.a.bitsize, 8)

        self.assertEqual(X.b.offset, 0)
        self.assertEqual(X.b.size, 1)
        self.assertEqual(X.b.bitsize, 4)

        self.assertEqual(X.c.offset, 0)
        self.assertEqual(X.c.size, 1)
        self.assertEqual(X

import ctypes
# Test ctypes.CField class.

from ctypes import *
import unittest

class X(ctypes.LittleEndianStructure):
    _fields_ = [("a", ctypes.c_byte, 8),
                ("b", ctypes.c_byte, 8)]

class Test(unittest.TestCase):
    def test_pack(self):
        # Test _pack_into() and from_buffer().

        # bytes
        b = bytearray(16)
        X._pack_into(b, 0, 1, 2)
        x = X.from_buffer(b, 0)
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, 2)
        self.assertEqual(X._sizeof(), 2)

        # array.array
        import array
        b = array.array('B', b'\0' * 16)
        X._pack_into(b, 0, 1, 2)
        x = X.from_buffer(b, 0)
        self.assertEqual(x.a, 1)

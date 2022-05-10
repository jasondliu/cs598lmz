import _struct
# Test _struct.Struct class

import binascii
import io
import sys
import unittest
from test import support

sys_big_endian = sys.byteorder == "big"

class StructTest(unittest.TestCase):

    def test_bool(self):
        # Issue #8014: pack() and unpack() should accept bool arguments
        s = _struct.Struct(b'?')
        self.assertEqual(s.pack(True), b'\x01')
        self.assertEqual(s.pack(False), b'\x00')
        self.assertEqual(s.unpack(b'\x01'), (True,))
        self.assertEqual(s.unpack(b'\x00'), (False,))
        self.assertRaises(TypeError, s.pack, 1)
        self.assertRaises(TypeError, s.unpack, b'\x01\x00')

    def test_format(self):
        # Test struct format strings
        s = _struct.Struct(b'xxxx')

import _struct
# Test _struct.Struct.

import struct
import sys
import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_struct_unpack(self):
        # Test _struct.Struct.unpack().
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x00\x00\x00\x00'), (0,))
        self.assertEqual(s.unpack(b'\xff\xff\xff\xff'), (-1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00', 1), (256,))
        self.assertRaises(struct.error, s.unpack, b'\x01\x00\x00')
        self.assertRaises(struct.error, s.unpack, b'\x01\x00\x00\x00', 2)


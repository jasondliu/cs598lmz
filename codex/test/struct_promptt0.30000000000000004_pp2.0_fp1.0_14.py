import _struct
# Test _struct.Struct.

import sys
import unittest
import struct
import _struct

class StructTest(unittest.TestCase):
    def test_struct(self):
        # Test _struct.Struct objects
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.pack(1), struct.pack('i', 1))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00', 0), (1,))
        self.assertEqual(s.unpack_from(b'\x01\x00\x00\x00', 1), (16777216,))

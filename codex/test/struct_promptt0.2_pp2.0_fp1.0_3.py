import _struct
# Test _struct.Struct.

import unittest
import sys
import struct

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct.
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.pack(1, 2), b'\x01\x00\x00\x00')
        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.pack, 1, 2, 3)
        self.assertRaises(struct.error, s.pack, 'abc')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))

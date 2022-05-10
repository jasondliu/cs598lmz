import _struct
# Test _struct.Struct

# Simple test of _struct.Struct

import sys
import struct
import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        # Simple test of _struct.Struct
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(12345), b'\x39\x30\x00\x00')
        self.assertEqual(s.unpack(b'\x39\x30\x00\x00'), (12345,))
        self.assertRaises(struct.error, s.unpack, b'hi')
        self.assertEqual(s.unpack_from(b'\x39\x30\x00\x00junk'), (12345,))
        self.assertRaises(struct.error, s.unpack_from, b'hijunk')

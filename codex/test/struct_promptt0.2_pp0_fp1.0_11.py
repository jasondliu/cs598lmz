import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import _testcapi

# Test _struct.Struct

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00', 0), (1,))
        self.assertEqual(s.unpack(b'xx\x01\x00\x00\x00xx', 2), (1,))
        self.assertEqual(s.unpack(b'xx\x01\x00\x00\x00xx', 2, 4), (1,))
        self.assertRaises(struct.error, s.unpack, b'\x01\x00\x00')

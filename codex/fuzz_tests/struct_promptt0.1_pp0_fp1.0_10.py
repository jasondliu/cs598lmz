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
        # Test _struct.Struct.unpack()
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01

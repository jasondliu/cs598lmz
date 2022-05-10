import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import _testcapi

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        # Test struct.unpack
        self.assertEqual(struct.unpack('i', b'\x00\x00\x00\x00'), (0,))
        self.assertEqual(struct.unpack('i', b'\x00\x00\x00\x01'), (1,))
        self.assertEqual(struct.unpack('i', b'\x00\x00\x00\xff'), (255,))
        self.assertEqual(struct.unpack('i', b'\x00\x00\x01\x00'), (256,))
        self.assertEqual(struct.unpack('i', b'\x00\x00\xff\x00'), (65280,))

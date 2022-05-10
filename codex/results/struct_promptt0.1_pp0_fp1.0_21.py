import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import _testcapi

# Test _struct.Struct

class StructTest(unittest.TestCase):

    def test_struct_bool(self):
        self.assertEqual(struct.pack('?', True), _struct.pack('?', True))
        self.assertEqual(struct.pack('?', False), _struct.pack('?', False))

    def test_struct_byteorder(self):
        self.assertEqual(struct.pack('@H', 1), _struct.pack('@H', 1))
        self.assertEqual(struct.pack('=H', 1), _struct.pack('=H', 1))
        self.assertEqual(struct.pack('<H', 1), _struct.pack('<H', 1))
        self.assertEqual(struct.pack('>H', 1), _struct.pack('>H', 1))
        self.assertEqual(struct.pack('!H', 1), _struct.pack('!H', 1))

    def test_struct

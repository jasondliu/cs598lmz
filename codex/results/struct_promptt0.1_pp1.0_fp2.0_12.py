import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import _testcapi

class StructTestCase(unittest.TestCase):

    def test_struct_bool(self):
        # Issue #1602
        self.assertEqual(struct.pack('?', True), b'\x01')
        self.assertEqual(struct.pack('?', False), b'\x00')
        self.assertEqual(struct.unpack('?', b'\x01')[0], True)
        self.assertEqual(struct.unpack('?', b'\x00')[0], False)

    def test_struct_bool_overflow(self):
        # Issue #1602
        self.assertRaises(struct.error, struct.pack, '?', -1)
        self.assertRaises(struct.error, struct.pack, '?', 256)
        self.assertRaises(struct.error, struct.pack, '?', 1.0)
        self.assertRaises(struct.error, struct.pack, '?', 1

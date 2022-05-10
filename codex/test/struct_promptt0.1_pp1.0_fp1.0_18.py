import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import _testcapi

class StructTestCase(unittest.TestCase):

    def test_struct_bool(self):
        # Issue #17072: struct.pack() should accept bool as an argument
        self.assertEqual(struct.pack('?', True), b'\x01')
        self.assertEqual(struct.pack('?', False), b'\x00')
        self.assertEqual(struct.pack('b', True), b'\x01')
        self.assertEqual(struct.pack('b', False), b'\x00')
        self.assertEqual(struct.pack('B', True), b'\x01')
        self.assertEqual(struct.pack('B', False), b'\x00')


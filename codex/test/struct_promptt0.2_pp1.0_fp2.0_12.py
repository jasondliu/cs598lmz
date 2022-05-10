import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import pickle
import copy

class StructTest(unittest.TestCase):

    def test_struct_bool(self):
        # Issue #17095: struct.pack() returns b'\x00' or b'\x01'
        # depending on the platform.
        self.assertEqual(struct.pack('?', False), b'\x00')
        self.assertEqual(struct.pack('?', True), b'\x01')

    def test_struct_bool_endian(self):
        # Issue #17095: struct.pack() returns b'\x00' or b'\x01'
        # depending on the platform.
        self.assertEqual(struct.pack('>?', False), b'\x00')
        self.assertEqual(struct.pack('>?', True), b'\x01')
        self.assertEqual(struct.pack('<?', False), b'\x00')

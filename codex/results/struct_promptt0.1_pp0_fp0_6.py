import _struct
# Test _struct.Struct.

import unittest
import sys
import struct
import io
import _testcapi

class StructTest(unittest.TestCase):

    def test_struct_bool(self):
        # Issue #15897: struct.pack() and struct.unpack() should accept bool
        # arguments.
        self.assertEqual(struct.pack('?', True), b'\x01')
        self.assertEqual(struct.pack('?', False), b'\x00')
        self.assertEqual(struct.unpack('?', b'\x01'), (True,))
        self.assertEqual(struct.unpack('?', b'\x00'), (False,))

    def test_struct_bool_overflow(self):
        # Issue #15897: struct.pack() and struct.unpack() should accept bool
        # arguments.
        self.assertRaises(OverflowError, struct.pack, '?', -1)
        self.assertRaises(OverflowError, struct.pack, '?', 2)
        self.assert

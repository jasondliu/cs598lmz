import _struct
# Test _struct.Struct

import unittest
import sys
import struct

from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack(self):
        # Test _struct.Struct.unpack()
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00', 1), (256,))
        self.assertRaises(struct.error, s.unpack, b'\x01\x00\x00')
        self.assertRaises(struct.error, s.unpack, b'\x01\x00\x00', 1)
        self.assertRaises(TypeError, s.unpack, None)
        self.assertRaises(TypeError, s.unpack, b'\x01\x00\x00\x00', None)
        self.assertRaises(TypeError

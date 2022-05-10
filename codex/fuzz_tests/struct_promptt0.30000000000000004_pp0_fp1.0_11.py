import _struct
# Test _struct.Struct.

import struct
import unittest

from test import support

class StructTestCase(unittest.TestCase):

    def test_basics(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, 'i')
        self.assertRaises(TypeError, s.pack, 'test')
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.unpack, 'test')
        self.assertRaises(TypeError, s.unpack, b'test')
        self.assertRaises(TypeError, s.unpack, b'test', 1, 2)
        self.assertRaises(struct.error, s.unpack, b'')
        self.assertRaises(struct.error, s.unpack, b'\x00')
        self.assertRaises(struct.error, s.unpack, b'\x00\x00\x00')
        self.

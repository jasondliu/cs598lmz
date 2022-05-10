import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import array

class StructTest(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertRaises(TypeError, s.pack, 'hi')
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.unpack, 'hi')
        self.assertRaises(TypeError, s.unpack, 1, 2)
        self.assertRaises(struct.error, s.pack)
        self.assertRaises(struct.error, s.pack, 1, 2, 3)
        self.assertRaises(struct.error, s.unpack)
        self.assertRaises(struct.error, s.unpack, 'hi')
        self.assertRaises(struct.error, s.unpack, 'h')



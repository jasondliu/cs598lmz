import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import _struct

class StructTest(unittest.TestCase):

    def test_basics(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertRaises(TypeError, s.__new__, _struct.Struct, 'i', 'j')
        self.assertRaises(TypeError, s.__new__, _struct.Struct, 1)
        self.assertRaises(TypeError, s.__new__, _struct.Struct, 1, 2, 3, 4)

    def test_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x00\x00\x00\x00'), (0,))
        self.assertEqual(s.unpack(b'\xff\xff\xff\xff'), (-1,))
        self.assertE

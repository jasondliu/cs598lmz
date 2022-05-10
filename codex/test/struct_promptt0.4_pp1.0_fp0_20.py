import _struct
# Test _struct.Struct

import unittest
from test import support
from test.support import bigmemtest


class StructTest(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.unpack, 'hi')
        self.assertRaises(TypeError, s.unpack)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.pack(-1), b'\xff\xff\xff\xff')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))

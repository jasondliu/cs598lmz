import _struct
# Test _struct.Struct

import struct
import sys

from test import support

class StructTest(unittest.TestCase):

    def test_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertRaises(struct.error, s.unpack, b'x')
        self.assertRaises(struct.error, s.unpack, b'\x01\x00\x00')

    def test_iter_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(list(s.iter_unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00')),
                         [(1,), (2,)])

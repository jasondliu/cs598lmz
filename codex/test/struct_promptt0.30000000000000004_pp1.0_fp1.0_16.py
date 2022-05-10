import _struct
# Test _struct.Struct.

import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertEqual(s.pack(1), _struct.pack('i', 1))
        self.assertEqual(s.unpack(_struct.pack('i', 1)), (1,))
        self.assertEqual(s.unpack_from(_struct.pack('i', 1), 0), (1,))
        self.assertEqual(s.unpack_from(_struct.pack('i', 1), 0, 1), (1,))
        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.unpack)
        self.assertRaises(TypeError, s.unpack, b'')

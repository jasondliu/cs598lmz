import _struct
# Test _struct.Struct objects

import array
import struct
import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct("i")
        self.assertEqual(s.size, struct.calcsize("i"))
        self.assertEqual(s.pack(1), struct.pack("i", 1))
        self.assertEqual(s.unpack(s.pack(1)), (1,))
        self.assertEqual(s.unpack_from(s.pack(1), 0), (1,))
        a = array.array("b", s.pack(1))
        self.assertEqual(s.unpack_from(a, 0), (1,))

        self.assertRaises(TypeError, s.pack)
        self.assertRaises(TypeError, s.pack, 1, 2)
        self.assertRaises(TypeError, s.pack, "abc")
        self.assertRaises(TypeError, s.unpack, "abc")
        self

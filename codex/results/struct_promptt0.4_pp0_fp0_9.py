import _struct
# Test _struct.Struct

import struct
import sys
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_basics(self):
        # Test _struct.Struct
        st = _struct.Struct("i")
        self.assertEqual(st.size, struct.calcsize("i"))
        self.assertEqual(st.format, "i")
        self.assertEqual(st.unpack(b"\x01\x00\x00\x00"), (1,))
        self.assertEqual(st.pack(1), b"\x01\x00\x00\x00")
        self.assertRaises(TypeError, st.unpack, b"\x01\x00\x00\x00"*2)
        self.assertRaises(TypeError, st.pack, 1, 2)
        self.assertRaises(TypeError, st.pack)
        self.assertRaises(TypeError, st.pack, None)
        self.assertRaises(TypeError, st.unpack,

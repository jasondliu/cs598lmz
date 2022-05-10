import _struct
# Test _struct.Struct, test the pack/unpack methods.

import struct
import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_struct(self):
        st = _struct.Struct('i')
        self.assertEqual(st.size, 4)
        self.assertEqual(st.pack(12345), struct.pack('i', 12345))
        self.assertEqual(st.unpack(st.pack(12345)), (12345,))

    def test_unpack_from(self):
        st = _struct.Struct('i')
        self.assertEqual(st.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00', 4),
                         (2,))

    def test_iter_unpack(self):
        st = _struct.Struct('i')

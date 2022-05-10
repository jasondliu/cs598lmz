import _struct
# Test _struct.Struct.

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct()
        st = _struct.Struct('hhl')
        self.assertEqual(st.size, 8)
        self.assertEqual(st.pack(1, 2, 3), b'\x01\x00\x02\x00\x00\x00\x00\x03')
        self.assertEqual(st.unpack(b'\x01\x00\x02\x00\x00\x00\x00\x03'), (1, 2, 3))
        self.assertEqual(st.pack_into(b'\x00'*8, 0, 1, 2, 3), None)
        self.assertEqual(b'\x01\x00\x02\x00\x00\x00\x00\x03',
                         b'\x00'*8)

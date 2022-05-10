import _struct
# Test _struct.Struct.

import io
import _struct
import unittest
import sys

class LittleEndianTest(unittest.TestCase):
    def test_bin_format(self):
        st = _struct.Struct('<hi')
        # integer
        self.assertEqual(st.pack(1234, 5678), b'G\xD2\x04\xD2\x86')
        self.assertEqual(st.unpack(b'G\xD2\x04\xD2\x86'), (1234, 5678))
        # overflow
        self.assertRaises(struct.error, st.pack, 0x1234, 0x56789abc)
        # underflow
        self.assertRaises(struct.error, st.unpack, b'G\xD2\x04\xD2')
        # negative integer
        self.assertEqual(st.pack(-1234, -5678), b'\xG2\xD2\xFC\x2D\x79')
        self.assertEqual(st

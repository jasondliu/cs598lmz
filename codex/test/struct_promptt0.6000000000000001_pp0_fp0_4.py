import _struct
# Test _struct.Struct.

import struct as st
import unittest
from test import support

def roundtrip(s, pack, unpack, value):
    result = s.pack(value)
    result = s.unpack(result)
    if result != value:
        raise ValueError('unpack failed roundtrip', value, result)

class StructTest(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.size, st.calcsize('i'))
        self.assertEqual(s.alignment, st.calcsize('i'))
        self.assertEqual(s.pack(12345), st.pack('i', 12345))
        self.assertEqual(s.unpack(st.pack('i', 54321)), (54321,))

        s = _struct.Struct('hhl')
        self.assertEqual(s.format, 'hhl')

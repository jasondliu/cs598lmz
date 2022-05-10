import _struct
# Test _struct.Struct.

import unittest
import sys
import struct
import io
import pickle
import copy
from test import support

class StructTestCase(unittest.TestCase):

    def test_basics(self):
        # Create a struct object
        st = _struct.Struct('hhl')

        # Check format, size, alignment
        self.assertEqual(st.format, 'hhl')
        self.assertEqual(st.size, 8)
        self.assertEqual(st.alignment, 4)

        # Try packing
        self.assertEqual(st.pack(1, 2, 3), b'\x01\x00\x02\x00\x00\x00\x00\x03')

        # Try unpacking
        self.assertEqual(st.unpack(b'\x01\x00\x02\x00\x00\x00\x00\x03'), (1, 2, 3))

        # Try iter unpacking
        self.assertEqual(list(st.iter_unpack(b'\x

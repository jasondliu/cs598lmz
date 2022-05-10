import _struct
# Test _struct.Struct

import unittest
import sys
import struct

from test import test_support

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        # Test _struct.Struct
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.pack(1), struct.pack('i', 1))
        self.assertEqual(s.unpack(s.pack(1)), (1,))
        self.assertEqual(s.unpack_from(s.pack(1), 0), (1,))
        self.assertEqual(s.unpack_from(s.pack(1)+s.pack(2), 0), (1,))
        self.assertEqual(s.unpack_from(s.pack(1)+s.pack(2), 4), (2,))
        self.assertEqual(s.pack_into(bytearray(8), 0, 1), None)
        self.assertEqual(

import _struct
# Test _struct.Struct

import unittest
import struct
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.pack(1), struct.pack('i', 1))
        self.assertEqual(s.unpack(s.pack(1)), (1,))
        self.assertEqual(s.unpack_from(s.pack(1), 0), (1,))
        self.assertEqual(s.unpack_from(s.pack(1), 0), (1,))
        self.assertEqual(s.unpack_from(memoryview(s.pack(1)), 0), (1,))
        self.assertEqual(s.pack_into(bytearray(4), 0, 1), None)
        self.assertEqual(s.pack_into(bytearray(4), 0, 1), None)
        self.

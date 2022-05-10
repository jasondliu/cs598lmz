import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        for code in 'bBhHiIlLqQfd':
            s = _struct.Struct(code)
            self.assertEqual(s.format, code)
            self.assertEqual(s.size, struct.calcsize(code))
            self.assertEqual(s.pack(0), struct.pack(code, 0))
            self.assertEqual(s.unpack(s.pack(0)), (0,))
            self.assertEqual(s.unpack_from(s.pack(0), 0), (0,))
            self.assertEqual(s.unpack(s.pack(1)), (1,))
            self.assertEqual(s.unpack_from(s.pack(1), 0), (1,))
            self.assertEqual(s.pack_into(bytearray(s.size), 0, 0), None)
            self.assertE

import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        s = _struct.Struct('hhl')
        self.assertEqual(s.size, 8)
        self.assertEqual(s.pack(1, 2, 3), b'\x01\x00\x02\x00\x00\x00\x00\x03')
        self.assertEqual(s.unpack(s.pack(1, 2, 3)), (1, 2, 3))

        # Issue #7995: struct.pack() should accept buffer objects
        self.assertEqual(s.pack_into(bytearray(s.size), 0, 1, 2, 3), None)
        self.assertEqual(s.unpack_from(bytearray(s.pack(1, 2, 3)), 0), (1, 2, 3))

        # Issue #7995: struct.pack_into() should accept buffer objects
        self.assertEqual

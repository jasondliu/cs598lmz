import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        s = _struct.Struct('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertEqual(s.pack(1), _struct.pack('i', 1))
        self.assertEqual(s.unpack(_struct.pack('i', 1)), (1,))
        self.assertEqual(s.pack_into(bytearray(), 0, 1), _struct.pack_into(
            'i', bytearray(), 0, 1))
        self.assertEqual(s.unpack_from(b'\x00\x00\x00\x01', 0), (1,))
        self.assertEqual(s.unpack_from(bytearray(b'\x00\x00\x00\x01'), 0), (1,))

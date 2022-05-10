import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack_from(self):
        # Issue #17078: struct.unpack_from() should accept a buffer object.
        buf = bytearray(b'abcdefgh')
        self.assertEqual(_struct.unpack_from('>H', buf, 3), (0x6543,))
        self.assertEqual(_struct.unpack_from('>H', buf, 3), (0x6543,))
        self.assertEqual(buf, bytearray(b'abcdefgh'))

    def test_struct_pack_into(self):
        # Issue #17078: struct.pack_into() should accept a buffer object.
        buf = bytearray(b'abcdefgh')
        _struct.pack_into('>H', buf, 3, 0x6543)
        self.assertEqual(buf, bytearray(b'abcdefgh'))
        _struct.pack_into

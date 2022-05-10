import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io
import _testcapi

# Test _struct.Struct

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        self.assertEqual(struct.Struct('i').size, 4)
        self.assertEqual(struct.Struct('i').pack(42), b'*\x00\x00\x00')
        self.assertEqual(struct.Struct('i').unpack(b'*\x00\x00\x00'), (42,))
        self.assertEqual(struct.Struct('i').unpack_from(b'\x00\x00\x00*', 0), (42,))
        self.assertEqual(struct.Struct('i').unpack_from(b'\x00\x00\x00*', 3), (42,))
        self.assertEqual(struct.Struct('i').unpack_from(b'\x00\x00\x00*', 4), (42,))

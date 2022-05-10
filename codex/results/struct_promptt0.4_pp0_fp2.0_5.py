import _struct
# Test _struct.Struct and _struct.pack_into

import sys
import unittest

from test.support import run_unittest

class StructTest(unittest.TestCase):
    def test_unpack_from(self):
        # Test unpacking from buffer
        data = b'\x12\x34\x56\x78\x9A\xBC\xDE\xF0'
        s = _struct.Struct('>Q')
        self.assertEqual(s.unpack_from(data, 0), (0x123456789ABCDEF0,))
        self.assertEqual(s.unpack_from(data, 1), (0x3456789ABCDEF09A,))
        self.assertEqual(s.unpack_from(data, 2), (0x56789ABCDEF09A34,))
        self.assertEqual(s.unpack_from(data, 3), (0x6789ABCDEF09A345,))
        self.assertEqual(s.unpack_from(data, 4), (0x789ABCDEF

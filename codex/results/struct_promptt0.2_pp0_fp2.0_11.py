import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        # Test _struct.Struct
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(12345), b'\x39\x30\x00\x00')
        self.assertEqual(s.unpack(b'\x39\x30\x00\x00'), (12345,))
        self.assertEqual(s.unpack_from(b'\x39\x30\x00\x00'), (12345,))
        self.assertEqual(s.unpack_from(b'\x39\x30\x00\x00', 0), (12345,))
        self.assertEqual(s.unpack_from(b'\x39\x30\x00\x00', 1), (0,))
        self.assertEqual(s.unpack_from(

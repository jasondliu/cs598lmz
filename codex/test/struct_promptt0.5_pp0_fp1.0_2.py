import _struct
# Test _struct.Struct

# This test is not very thorough, it just makes sure that the
# basic operations work and that the data returned is of the
# correct size and type.

import sys
import unittest
from test import support
from struct import Struct

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        s = _struct.Struct("hhl")
        self.assertEqual(s.size, 8)
        self.assertEqual(s.format, "hhl")
        self.assertEqual(s.unpack("abcdefgh"), (25185, 25699, 50331648))
        self.assertEqual(s.pack(1, 2, 3), b"\x00\x01\x00\x02\x00\x00\x00\x03")
        self.assertEqual(s.unpack_from(b"abcdefgh", 3), (25699, 50331648))
        self.assertEqual(s.calcsize(), 8)

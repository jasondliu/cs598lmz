import _struct
# Test _struct.Struct
# Issue #16574

import _testcapi
import struct
import sys

class StructTest(unittest.TestCase):

    def test_Struct(self):
        s = _struct.Struct("hhl")
        self.assertEqual(s.size, struct.calcsize("hhl"))
        self.assertEqual(s.format, "hhl")
        self.assertEqual(s.pack(*range(3)), b"\x00\x00\x00\x01\x00\x02\x00\x00\x00")
        self.assertEqual(s.pack_into(bytearray(8), 0, *range(3)), 8)
        self.assertEqual(s.unpack(b"\x00\x00\x00\x01\x00\x02\x00\x00\x00"), (0, 1, 2))
        self.assertEqual(s.unpack_from(b"\x00\x00\x00\x01\x00\x02\x00\x

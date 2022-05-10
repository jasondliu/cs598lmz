import _struct
# Test _struct.Struct
#
# This test is a bit different from the others.  It is a bit of a
# torture test for the _struct module, and also serves as a regression
# test for bugs found in earlier versions.  The test data is a bit
# fragile, and may need to be updated if bugs are found.

import _struct
import unittest
from test import support
import sys
import struct

class StructTest(unittest.TestCase):
    def test_basics(self):
        # Create a struct object
        st = _struct.Struct("i")
        self.assertEqual(st.size, 4)
        self.assertEqual(st.format, "i")

        # Try packing
        self.assertEqual(st.pack(12345), b"\x39\x30\x00\x00")

        # Try unpacking
        self.assertEqual(st.unpack(b"\x39\x30\x00\x00"), (12345,))
        self.assertEqual(st.unpack_from(b"\x39\x

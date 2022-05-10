import _struct
# Test _struct.Struct
#
# This test verifies that the _struct module works as expected.
#
# It also tests the struct module, but not as thoroughly as test_struct.py

import sys
import unittest
import struct

from test import support

# The _struct module is an implementation detail and not part of the
# public API.  It is tested here to ensure that it works as expected.

class StructTest(unittest.TestCase):
    def test_struct(self):
        # Test the _struct module
        s = _struct.Struct("i")
        self.assertEqual(s.size, 4)
        self.assertEqual(s.format, "i")
        self.assertEqual(s.pack(1), b"\x01\x00\x00\x00")
        self.assertEqual(s.unpack(b"\x01\x00\x00\x00"), (1,))

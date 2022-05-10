import _struct
# Test _struct.Struct

# This is a test of the _struct module.
# This is a test of the _struct module.
# This is a test of the _struct module.

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_pack(self):
        # Test pack.
        self.assertEqual(_struct.pack("h", 1), b"\x00\x01")
        self.assertEqual(_struct.pack("h", 128), b"\x00\x80")
        self.assertEqual(_struct.pack("h", -129), b"\xff\x7f")

        self.assertEqual(_struct.pack("h", 0x1234), b"\x12\x34")
        self.assertEqual(_struct.pack("h", -0x1234), b"\xed\xcc")

        self.assertEqual(_struct.pack("b", 1), b"\x01")

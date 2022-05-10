import _struct
# Test _struct.Struct class
#
import array
import sys

import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_struct(self):
        self.assertEqual(_struct.pack("si", b'AB', 10),
            b'AB\x00\x00\x00\n\x00\x00\x00')
        self.assertEqual(_struct.pack("si", b'A'*100, 10),
            b'A'*100 + b'\n\x00\x00\x00')
        self.assertEqual(_struct.unpack("si", b'AB\x00\x00\x00\n\x00\x00\x00'),
            (b'AB', 10))
        self.assertEqual(_struct.pack("i", -1), b'\xff\xff\xff\xff')
        self.assertRaises(TypeError, _struct.pack, "s", 1)

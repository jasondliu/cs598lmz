import _struct
# Test _struct.Struct objects.

import struct
import sys
import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_format(self):
        with self.assertRaises(TypeError):
            _struct.Struct(b"<2s")
        self.assertEqual(_struct.Struct("abc").format, "abc")
        self.assertEqual(_struct.Struct("<abc").format, "<abc")
        self.assertEqual(_struct.Struct(">abc").format, ">abc")

    def test_size(self):
        self.assertEqual(_struct.Struct("").size, 0)
        self.assertEqual(_struct.Struct("i").size, 4)
        self.assertEqual(_struct.Struct("<i").size, 4)
        self.assertEqual(_struct.Struct("<i").size, 4)
        self.assertEqual(_struct.Struct("@i").size, 4)
        self.assertEqual(_struct.Struct("=i").size, 4)

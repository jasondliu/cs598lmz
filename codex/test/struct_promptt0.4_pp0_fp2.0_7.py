import _struct
# Test _struct.Struct.

import struct
import sys
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_format_size(self):
        # Test _struct.Struct.format_size()
        s = _struct.Struct("hhl")
        self.assertEqual(s.size, s.format_size("<hhl"))
        self.assertEqual(s.size, s.format_size("@hhl"))
        self.assertEqual(s.size, s.format_size(">hhl"))
        self.assertRaises(TypeError, s.format_size, 42)
        self.assertRaises(TypeError, s.format_size, "")
        self.assertRaises(TypeError, s.format_size, "hhl")

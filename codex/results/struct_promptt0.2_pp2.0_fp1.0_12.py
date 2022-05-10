import _struct
# Test _struct.Struct.

import unittest
import sys
import struct

class StructTest(unittest.TestCase):

    def test_format_size(self):
        # Test format_size()
        self.assertEqual(_struct.format_size('@'), 0)
        self.assertEqual(_struct.format_size('=i'), 4)
        self.assertEqual(_struct.format_size('<i'), 4)
        self.assertEqual(_struct.format_size('>i'), 4)
        self.assertEqual(_struct.format_size('!i'), 4)
        self.assertEqual(_struct.format_size('x'), 1)
        self.assertEqual(_struct.format_size('c'), 1)
        self.assertEqual(_struct.format_size('b'), 1)
        self.assertEqual(_struct.format_size('B'), 1)
        self.assertEqual(_struct.format_size('h'), 2)
        self.assertEqual(_struct.format_size('H'), 2)
        self.assertEqual(_struct

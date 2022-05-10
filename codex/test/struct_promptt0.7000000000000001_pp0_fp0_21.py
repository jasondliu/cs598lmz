import _struct
# Test _struct.Struct.

import _struct as struct
import io
import unittest
from test import support
import sys
import copy

class StructTest(unittest.TestCase):
    # Issue7998: struct.Struct has no way to get the format used to
    # instantiate it.
    def test_format(self):
        self.assertEqual(struct.Struct('hi').format, 'hi')
        self.assertEqual(struct.Struct('hi').size, 4)
        self.assertEqual(struct.Struct('xcb').format, 'xcb')
        self.assertEqual(struct.Struct('xcb').size, 1)
        self.assertEqual(struct.Struct('i').format, 'i')
        self.assertEqual(struct.Struct('i').size, 4)
        self.assertEqual(struct.Struct('l').format, 'l')
        self.assertEqual(struct.Struct('l').size, 8)
        self.assertEqual(struct.Struct('q').format, 'q')

import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_format_size(self):
        # Issue #1763: _struct.calcsize() should raise TypeError for bad formats
        self.assertRaises(TypeError, _struct.calcsize, b'Z')
        self.assertRaises(TypeError, _struct.calcsize, b'Z9')
        self.assertRaises(TypeError, _struct.calcsize, b'bZ')
        self.assertRaises(TypeError, _struct.calcsize, b'b9Z')
        self.assertRaises(TypeError, _struct.calcsize, b'b9')
        self.assertRaises(TypeError, _struct.calcsize, b'b')
        self.assertRaises(TypeError, _struct.calcsize, b'9')
        self.assertRaises(TypeError, _struct.calcsize, b'bP')

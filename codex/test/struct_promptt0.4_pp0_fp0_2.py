import _struct
# Test _struct.Struct.

import unittest
import sys
import struct

from test import test_support

class StructTestCase(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 1, 2, 3)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', format='ghi')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', format='ghi', new='jkl')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', format='ghi', new=1)

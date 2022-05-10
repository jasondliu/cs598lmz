import _struct
# Test _struct.Struct

import unittest
from test import test_support
import sys

class StructTestCase(unittest.TestCase):

    def test_bool(self):
        self.assertRaises(TypeError, _struct.Struct, '?')
        self.assertRaises(TypeError, _struct.Struct, '?', True)

    def test_format(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 1)
        self.assertRaises(TypeError, _struct.Struct, 'abc')
        self.assertRaises(TypeError, _struct.Struct, 'abc', True)

    def test_sizeof(self):
        self.assertEqual(_struct.Struct('x').size, 1)
        self.assertEqual(_struct.Struct('cb?').size, 4)
        self.assertEqual(_struct.Struct('cb?xx').size, 6)
        self.assertEqual(_struct.Struct('cb?xx').size, 6)
        self.assertEqual

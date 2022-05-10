import _struct
# Test _struct.Struct

import sys
import unittest

from test import support

class StructTestCase(unittest.TestCase):
    def test_format(self):
        self.assertEqual(_struct.Struct('x').format, 'x')
        self.assertEqual(_struct.Struct('cb').format, 'cb')
        self.assertEqual(_struct.Struct('hhl').format, 'hhl')
        self.assertEqual(_struct.Struct('hhh').format, 'hhh')
        self.assertEqual(_struct.Struct('bBhHiIlLqQfd').format, 'bBhHiIlLqQfd')
        self.assertRaises(TypeError, _struct.Struct, 123)
        self.assertRaises(TypeError, _struct.Struct, 'x', 123)
        self.assertRaises(TypeError, _struct.Struct, 'x', 'y')
        self.assertRaises(TypeError, _struct.Struct, 'x', 123, 456)
        self.assertRaises(ValueError, _struct.Struct, '')
       

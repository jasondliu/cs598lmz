import _struct
# Test _struct.Struct
import unittest
from test import support

class AllTests(unittest.TestCase):

    def test_error(self):
        self.assertRaises(TypeError, _struct.Struct('abc').pack, 2)
        self.assertRaises(TypeError, _struct.Struct('').pack)
        self.assertRaises(TypeError, _struct.Struct('i').pack, 1, 2, 3)
        self.assertRaises(TypeError, _struct.Struct('i').pack, 'a')
        self.assertRaises(TypeError, _struct.Struct('P').pack, 'a')
        self.assertRaises(TypeError, _struct.Struct('P').pack, 1)
        self.assertRaises(TypeError, _struct.Struct('P').pack, 1, 2)
        self.assertRaises(TypeError, _struct.Struct('P').pack)
        self.assertRaises(TypeError, _struct.Struct('x').pack)
        self.assertRaises(TypeError, _struct.Struct('xi').pack, 1)


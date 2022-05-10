import _struct
# Test _struct.Struct

import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('abcj')
        with self.assertRaises(TypeError):
            _struct.Struct('abcdefghijklmnopqrstuvwxyz')
        with self.assertRaises(TypeError):
            _struct.Struct('abcdefghijklmnopqrstuvwxyz', 0)
        with self.assertRaises(TypeError):
            _struct.Struct('abcdefghijklmnopqrstuvwxyz', '0')
        with self.assertRaises(TypeError):
            _struct.Struct('abcdefghijklmnopqrstuvwxyz', '0', 0)

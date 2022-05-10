import _struct
# Test _struct.Struct.

import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('', '')
        with self.assertRaises(TypeError):
            _struct.Struct('', '', '')
        with self.assertRaises(TypeError):
            _struct.Struct('', '', '', '')
        with self.assertRaises(TypeError):
            _struct.Struct('', '', '', '', '')
        with self.assertRaises(TypeError):
            _struct.Struct('', '', '', '', '', '')
        with self.assertRaises(TypeError):
            _struct.Struct('', '', '', '', '', '', '')
        with self.assertRaises(TypeError):
            _struct.Struct('',

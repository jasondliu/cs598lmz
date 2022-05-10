import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct(self):
        with self.assertRaises(TypeError):
            _struct.Struct()
        with self.assertRaises(TypeError):
            _struct.Struct('')
        with self.assertRaises(TypeError):
            _struct.Struct('', 0)
        with self.assertRaises(TypeError):
            _struct.Struct('', 0, 0)
        with self.assertRaises(TypeError):
            _struct.Struct('', 0, 0, 0)
        with self.assertRaises(TypeError):
            _struct.Struct('', 0, 0, 0, 0)
        with self.assertRaises(TypeError):
            _struct.Struct('', 0, 0, 0, 0, 0)
        with self.assertRaises(TypeError):
            _struct.Struct('', 0, 0, 0, 0, 0, 0)
        with self.assertRaises(TypeError):
            _struct.Struct('',

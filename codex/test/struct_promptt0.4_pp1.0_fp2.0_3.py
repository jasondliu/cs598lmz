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
            _struct.Struct('', 10)
        with self.assertRaises(TypeError):
            _struct.Struct('', 'little')
        with self.assertRaises(TypeError):
            _struct.Struct('', 'little', 10)
        with self.assertRaises(TypeError):
            _struct.Struct('', 'little', 'unsigned')
        with self.assertRaises(TypeError):
            _struct.Struct('', 'little', 'unsigned', 10)
        with self.assertRaises(TypeError):
            _struct.Struct('', 'little', 'unsigned', 'char')

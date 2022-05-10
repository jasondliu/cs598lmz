import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi')

    def test_struct_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))
        self.assertRaises(TypeError, s.unpack, '\x01\x00\x00\x00')
        self.assertRaises(TypeError, s.unpack, memoryview(b'\x01\x00\x00\x00'))

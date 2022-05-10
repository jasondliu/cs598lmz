import _struct
# Test _struct.Struct objects.

import struct
import sys
import test.support
import unittest

# Test the Struct class.

class StructTest(unittest.TestCase):

    def test_struct_object(self):
        st = _struct.Struct('l')
        self.assertEqual(st.size, _struct.calcsize('l'))
        self.assertEqual(st.format, 'l')
        self.assertRaises(TypeError, st.__delattr__, 'size')
        self.assertRaises(TypeError, st.__delattr__, 'format')
        self.assertRaises(TypeError, st.__delattr__, 'pack')

    def test_struct_error(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 1)
        self.assertRaises(TypeError, _struct.Struct, 'l', 'l')
        self.assertRaises(TypeError, _struct.Struct, 'l', 1)
        self.assertRa

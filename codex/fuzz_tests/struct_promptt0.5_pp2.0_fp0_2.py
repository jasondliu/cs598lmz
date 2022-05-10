import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

def get_integer_size():
    # Return size of C 'int' and 'long' in bytes.
    return _struct.calcsize('i')

def get_float_size():
    # Return size of C 'float' and 'double' in bytes.
    return _struct.calcsize('d')

class StructTest(unittest.TestCase):

    def test_unpack_from(self):
        # Test the '_struct.Struct.unpack_from()' method.
        s = _struct.Struct(b'hi')
        data = b'ab'
        self.assertEqual(s.unpack_from(data), (25185, 25699))
        self.assertEqual(s.unpack_from(data, 1), (25699,))
        self.assertEqual(s.unpack_from(memoryview(data), 1), (25699,))
        self.assertRaises(struct.error, s.unpack_from, b'a')
        self

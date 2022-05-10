import _struct
# Test _struct.Struct.__new__()

import sys
import unittest
from test import support

# Test the Struct.__new__() method.

class StructNewTest(unittest.TestCase):
    def test_constructor(self):
        # test the constructor
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, '', 42)
        self.assertRaises(TypeError, _struct.Struct, '', 'not a format')
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.pack(42), struct.pack('i', 42))

    def test_copy(self):
        # test the copy method
        s = _struct.Struct('i')
        c = s.copy()
        self.assertEqual(s.format, c.format)

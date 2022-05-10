import _struct
# Test _struct.Struct.__new__()

import _struct
import unittest

class StructTest(unittest.TestCase):

    def test_new(self):
        self.assertRaises(TypeError, _struct.Struct)
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr')
        self.assertRaises(TypeError, _struct.Struct, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu')
        self.assertRaises(Type

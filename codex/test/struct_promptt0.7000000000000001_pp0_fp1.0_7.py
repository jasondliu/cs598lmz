import _struct
# Test _struct.Struct.

import _struct
import unittest
from test.test_support import run_unittest

class StructTest(unittest.TestCase):
    def test_format_size(self):
        self.assertRaises(TypeError, _struct.calcsize, object())
        self.assertRaises(TypeError, _struct.calcsize, 123)

    def test_format_char_validation(self):
        _struct.calcsize('qQ')
        self.assertRaises(TypeError, _struct.calcsize, '!')
        self.assertRaises(TypeError, _struct.calcsize, '=')
        self.assertRaises(TypeError, _struct.calcsize, '@')
        self.assertRaises(TypeError, _struct.calcsize, '<>')
        self.assertRaises(TypeError, _struct.calcsize, '!@')
        self.assertRaises(TypeError, _struct.calcsize, '@!')

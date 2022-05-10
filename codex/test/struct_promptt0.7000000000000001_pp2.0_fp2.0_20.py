import _struct
# Test _struct.Struct.

import unittest
from test import support
from test import test_struct
from test.support import import_module

from io import BytesIO
from sys import getsizeof

class StructTest(test_struct.StructTest):

    def test_format_sizeof(self):
        types = 'bBhHiIlLqQfd'
        formats = '@=<>! ' + types
        for code in formats:
            s = _struct.Struct(code)
            size = struct.calcsize(code)
            self.assertEqual(s.size, size)
            self.assertEqual(getsizeof(s), getsizeof(s.format) - 24)
            self.assertEqual(s.format, code)

    def test_error_cases(self):
        f = _struct.Struct
        self.assertRaises(TypeError, f)
        self.assertRaises(TypeError, f, 'P', 42)
        self.assertRaises(TypeError, f, 42, 42)

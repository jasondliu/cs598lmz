import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):
    def test_struct(self):
        s = _struct.Struct('i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x00\x00'), (1,))

    def test_struct_format(self):
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.format_char, 'i')
        self.assertEqual(s.format_description, 'int')

        s = _struct.Struct('q')
        self.assertEqual(s.format, 'q')
        self.assertEqual(s.format_char, 'q')
        self.assertEqual(s.format_description, 'long long')


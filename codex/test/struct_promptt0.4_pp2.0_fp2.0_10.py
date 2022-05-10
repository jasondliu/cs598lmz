import _struct
# Test _struct.Struct

import unittest
import sys
import struct
import io

# The standard struct module is used to generate the expected results.

class StructTestCase(unittest.TestCase):

    def test_format_size_alignment(self):
        fmt = 'hhl'
        expected_size = struct.calcsize(fmt)
        expected_alignment = struct.calcsize('ii') - struct.calcsize('i')
        s = _struct.Struct(fmt)
        self.assertEqual(s.size, expected_size)
        self.assertEqual(s.alignment, expected_alignment)

    def test_format_error(self):
        self.assertRaises(struct.error, _struct.Struct, 'z')
        self.assertRaises(struct.error, _struct.Struct, 'P')
        self.assertRaises(struct.error, _struct.Struct, 'P#')


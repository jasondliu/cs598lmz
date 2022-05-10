import _struct
# Test _struct.Struct() class
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_struct_without_format(self):
        with self.assertRaises(TypeError):
            _struct.Struct()

    def test_struct_with_bad_format(self):
        with self.assertRaises(TypeError):
            _struct.Struct(42)

    def test_struct_with_bad_format(self):
        with self.assertRaises(_struct.StructError):
            _struct.Struct('Q')

    def test_struct_with_format(self):
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.alignment, struct.calcsize('i'))

    def test_unpack_with_bad_buffer(self):
        s = _struct.Struct('i')

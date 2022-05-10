import _struct
# Test _struct.Struct() method
#
import _struct
import unittest


class StructTest(unittest.TestCase):

    def test_format(self):
        # Invalid format
        self.assertRaises(ValueError, _struct.Struct, 'z')
        self.assertRaises(ValueError, _struct.Struct, 'z9')
        self.assertRaises(ValueError, _struct.Struct, 'z!')
        self.assertRaises(ValueError, _struct.Struct, '9')
        self.assertRaises(ValueError, _struct.Struct, '!')

    def test_size(self):
        # Invalid size
        self.assertRaises(ValueError, _struct.Struct, '')
        self.assertRaises(ValueError, _struct.Struct, '@P')
        self.assertRaises(ValueError, _struct.Struct, '@P0')
        self.assertRaises(ValueError, _struct.Struct, '@P0s')
        self.assertRaises(ValueError, _struct.Struct, '@0s')
        self

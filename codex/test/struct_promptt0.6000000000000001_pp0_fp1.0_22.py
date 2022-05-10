import _struct
# Test _struct.Struct
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_format(self):
        self.assertEqual(_struct.Struct('i').format, 'i')
        self.assertEqual(_struct.Struct('ii').format, 'ii')
        self.assertEqual(_struct.Struct('bbbb').format, 'bbbb')
        self.assertEqual(_struct.Struct('hhh').format, 'hhh')
        self.assertEqual(_struct.Struct('hhh').size, 3)
        self.assertEqual(_struct.Struct('bBhHiIlLqQfd').format, 'bBhHiIlLqQfd')
        self.assertRaises(TypeError, _struct.Struct, 'z')
        self.assertRaises(TypeError, _struct.Struct, 'bBhHiIlLqQfdz')

    def test_size(self):
        self.assertEqual(_struct.Struct('i').size, _struct.calcsize('i'))

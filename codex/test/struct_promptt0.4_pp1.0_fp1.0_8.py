import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_format(self):
        self.assertEqual(_struct.Struct('i').format, 'i')
        self.assertEqual(_struct.Struct('ii').format, 'ii')
        self.assertEqual(_struct.Struct('hhh').format, 'hhh')
        self.assertEqual(_struct.Struct('bBhHiIlLqQfd').format, 'bBhHiIlLqQfd')
        self.assertEqual(_struct.Struct('xxxx').format, 'xxxx')

    def test_size(self):
        self.assertEqual(_struct.Struct('i').size, 4)
        self.assertEqual(_struct.Struct('ii').size, 8)
        self.assertEqual(_struct.Struct('hhh').size, 6)
        self.assertEqual(_struct.Struct('bBhHiIlLqQfd').size, 23)
        self.assertEqual(_struct.Struct('xxxx').size, 4)


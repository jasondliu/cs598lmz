import _struct
# Test _struct.Struct

import unittest
from test import support
from struct import Struct

class StructTest(unittest.TestCase):
    def test_format(self):
        self.assertEqual(_struct.Struct('c').format, 'c')
        self.assertEqual(_struct.Struct('bb').format, 'bb')
        self.assertEqual(_struct.Struct('hhh').format, 'hhh')
        self.assertEqual(_struct.Struct('iii').format, 'iii')
        self.assertEqual(_struct.Struct('qqq').format, 'qqq')
        self.assertEqual(_struct.Struct('ccc').format, 'ccc')
        self.assertEqual(_struct.Struct('fff').format, 'fff')
        self.assertEqual(_struct.Struct('ddd').format, 'ddd')
        self.assertEqual(_struct.Struct('P').format, 'P')
        self.assertEqual(_struct.Struct('s').format, 's')
        self.assertEqual(_struct.Struct('p').format, 'p')
        self

import _struct
# Test _struct.Struct

import unittest
from test import test_support

class StructTestCase(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('l'), 4)
        self.assertEqual(_struct.calcsize('q'), 8)
        self.assertEqual(_struct.calcsize('h'), 2)
        self.assertEqual(_struct.calcsize('H'), 2)
        self.assertEqual(_struct.calcsize('P'), 4)
        self.assertEqual(_struct.calcsize('Q'), 8)
        self.assertEqual(_struct.calcsize('f'), 4)
        self.assertEqual(_struct.calcsize('d'), 8)
        self.assertEqual(_struct.calcsize('s'), 1)
        self.assertEqual(_struct.calcsize('p'), 1)
        self.assertEqual(_struct.calcsize('x'), 1)
       

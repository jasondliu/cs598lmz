import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_format_size(self):
        # Issue #1202
        self.assertEqual(_struct.calcsize('b'), 1)
        self.assertEqual(_struct.calcsize('B'), 1)
        self.assertEqual(_struct.calcsize('c'), 1)
        self.assertEqual(_struct.calcsize('?'), 1)
        self.assertEqual(_struct.calcsize('h'), 2)
        self.assertEqual(_struct.calcsize('H'), 2)
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('I'), 4)
        self.assertEqual(_struct.calcsize('l'), 4)
        self.assertEqual(_struct.calcsize('L'), 4)
        self.assertEqual(_struct.calcsize('q'), 8)
        self.assertEqual(_struct.calcsize('Q'),

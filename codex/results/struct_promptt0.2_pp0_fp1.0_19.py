import _struct
# Test _struct.Struct

# Test _struct.Struct

import _struct
import unittest
import sys
import struct

class StructTest(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(_struct.calcsize('b'), 1)
        self.assertEqual(_struct.calcsize('h'), 2)
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('l'), 4)
        self.assertEqual(_struct.calcsize('q'), 8)
        self.assertEqual(_struct.calcsize('B'), 1)
        self.assertEqual(_struct.calcsize('H'), 2)
        self.assertEqual(_struct.calcsize('I'), 4)
        self.assertEqual(_struct.calcsize('L'), 4)
        self.assertEqual(_struct.calcsize('Q'), 8)
        self.assertEqual(_struct.calcsize('f'), 4)
        self.assertEqual(_struct.

import _struct
# Test _struct.Struct

import sys
import unittest
import _struct
import struct
import test.support

class StructTestCase(unittest.TestCase):
    def test_format_size(self):
        self.assertRaises(struct.error, _struct.calcsize, '1')
        self.assertRaises(struct.error, _struct.calcsize, '1z')

        self.assertEqual(_struct.calcsize('x'), 1)
        self.assertEqual(_struct.calcsize('c'), 1)
        self.assertEqual(_struct.calcsize('b'), 1)
        self.assertEqual(_struct.calcsize('B'), 1)
        self.assertEqual(_struct.calcsize('?'), 1)
        self.assertEqual(_struct.calcsize('h'), 2)
        self.assertEqual(_struct.calcsize('H'), 2)
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('I'), 4)
        self

import _struct
# Test _struct.Struct methods

import unittest
from test import support

import _struct

class StructTestCase(unittest.TestCase):

    def test_sizeof(self):
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('l'), 4)
        self.assertEqual(_struct.calcsize('q'), 8)
        self.assertEqual(_struct.calcsize('h'), 2)
        self.assertEqual(_struct.calcsize('P'), 4)
        self.assertEqual(_struct.calcsize('P', '!='), 8)

    def test_sizeof_format(self):
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('iP'), 8)
        self.assertEqual(_struct.calcsize('P', '!='), 8)
        self.assertEqual(_struct.calcsize('P', '!=', 3), 24)

    def test_unpack(

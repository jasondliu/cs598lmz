import _struct
# Test _struct.Struct.

from test import test_support
import unittest

class StructTestCase(unittest.TestCase):

    def test_format_sizeof(self):
        self.assertEqual(_struct.calcsize('s'), 1)
        self.assertEqual(_struct.calcsize('s#'), 1)
        self.assertEqual(_struct.calcsize('c'), 1)
        self.assertEqual(_struct.calcsize('b'), 1)
        self.assertEqual(_struct.calcsize('b#'), 1)
        self.assertEqual(_struct.calcsize('B'), 1)
        self.assertEqual(_struct.calcsize('B#'), 1)
        self.assertEqual(_struct.calcsize('h'), 2)
        self.assertEqual(_struct.calcsize('h#'), 2)
        self.assertEqual(_struct.calcsize('H'), 2)
        self.assertEqual(_struct.calcsize('H#'), 2)

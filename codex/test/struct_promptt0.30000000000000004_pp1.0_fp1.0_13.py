import _struct
# Test _struct.Struct with all types

import _struct
import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_format_size(self):
        # Test that the format string is parsed correctly
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('iI'), 8)
        self.assertEqual(_struct.calcsize('hi'), 4)
        self.assertEqual(_struct.calcsize('ih'), 4)
        self.assertEqual(_struct.calcsize('hhh'), 3)
        self.assertEqual(_struct.calcsize('hhhh'), 4)
        self.assertEqual(_struct.calcsize('hhi'), 4)
        self.assertEqual(_struct.calcsize('h'), 2)
        self.assertEqual(_struct.calcsize('H'), 2)

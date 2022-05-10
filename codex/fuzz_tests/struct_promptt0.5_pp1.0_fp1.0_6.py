import _struct
# Test _struct.Struct.
import unittest
import sys

class StructTestCase(unittest.TestCase):

    def test_format_size(self):
        # Test format string size calculation.
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('ihb'), 8)
        self.assertEqual(_struct.calcsize('ihb'), _struct.calcsize('hi'))
        self.assertEqual(_struct.calcsize('hi'), _struct.calcsize('h'))
        self.assertEqual(_struct.calcsize('h'), _struct.calcsize('b'))
        self.assertEqual(_struct.calcsize('b'), 1)
        self.assertEqual(_struct.calcsize('b'), _struct.calcsize('c'))
        self.assertEqual(_struct.calcsize('b'), _struct.calcsize('?'))
        self.assertEqual(_struct.calcsize('b'), _struct.calcsize('B'))
       

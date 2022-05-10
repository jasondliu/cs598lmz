import _struct
# Test _struct.Struct class.
import struct
import sys
import unittest
import warnings
from test import support

class StructTest(unittest.TestCase):
    def test_struct(self):
        self.assertEqual(struct.calcsize('i'), _struct.calcsize('i'))
        self.assertEqual(struct.calcsize('i4s'), _struct.calcsize('i4s'))
        self.assertEqual(struct.calcsize('4si'), _struct.calcsize('4si'))
        self.assertEqual(struct.calcsize('4sI'), _struct.calcsize('4sI'))
        self.assertEqual(struct.calcsize('i4sI'), _struct.calcsize('i4sI'))
        self.assertEqual(struct.calcsize('i4sh'), _struct.calcsize('i4sh'))
        self.assertEqual(struct.calcsize('i4sIh'), _struct.calcsize('i4sIh'))
        self

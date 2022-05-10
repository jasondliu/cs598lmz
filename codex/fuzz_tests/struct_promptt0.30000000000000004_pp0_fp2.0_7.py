import _struct
# Test _struct.Struct.__repr__

from test.support import run_unittest
import unittest
import sys

class StructTest(unittest.TestCase):

    def test_repr(self):
        self.assertEqual(repr(_struct.Struct('i')),
                         "<class '_struct.Struct'>('i')")
        self.assertEqual(repr(_struct.Struct('ii')),
                         "<class '_struct.Struct'>('ii')")
        self.assertEqual(repr(_struct.Struct('<i')),
                         "<class '_struct.Struct'>('<i')")
        self.assertEqual(repr(_struct.Struct('>i')),
                         "<class '_struct.Struct'>('>i')")
        self.assertEqual(repr(_struct.Struct('=i')),
                         "<class '_struct.Struct'>('=i')")
        self.assertEqual(repr(_struct.Struct('!i')),
                         "<class '_struct.Struct'>('!i')")
        self.assertEqual(

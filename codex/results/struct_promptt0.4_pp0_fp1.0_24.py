import _struct
# Test _struct.Struct.

import unittest
import sys
import struct

class StructTest(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(struct.calcsize('h'), _struct.Struct('h').size)
        self.assertEqual(struct.calcsize('hh'), _struct.Struct('hh').size)
        self.assertEqual(struct.calcsize('hhh'), _struct.Struct('hhh').size)
        self.assertEqual(struct.calcsize('i'), _struct.Struct('i').size)
        self.assertEqual(struct.calcsize('ii'), _struct.Struct('ii').size)
        self.assertEqual(struct.calcsize('iii'), _struct.Struct('iii').size)
        self.assertEqual(struct.calcsize('l'), _struct.Struct('l').size)
        self.assertEqual(struct.calcsize('ll'), _struct.Struct('ll').size)
        self.assertEqual(struct.calcsize('lll'), _struct

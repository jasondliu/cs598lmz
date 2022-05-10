import _struct
# Test _struct.Struct.__repr__ and _struct.Struct.format

import sys
import test.test_support
import unittest

class StructTest(unittest.TestCase):

    def test_repr(self):
        s = _struct.Struct('i')
        self.assertEqual(repr(s), "<_struct.Struct object at %#x>" % id(s))
        s = _struct.Struct('ci')
        self.assertEqual(repr(s), "<_struct.Struct object at %#x>" % id(s))
        s = _struct.Struct('4s')
        self.assertEqual(repr(s), "<_struct.Struct object at %#x>" % id(s))

    def test_format(self):
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        s = _struct.Struct('ci')
        self.assertEqual(s.format, 'ci')
        s = _struct.Struct('4s')
        self.assertEqual(s.format

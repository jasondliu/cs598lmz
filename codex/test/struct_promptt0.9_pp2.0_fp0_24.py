import _struct
# Test _struct.Struct objects.
from test import support
import unittest
import sys
from decimal import Decimal
from fractions import Fraction


class StructTest(unittest.TestCase):
    def test_creation(self):
        formats = "bi?"
        expected_sizeof = 10
        expected_alignment = 4
        d = _struct.calcsize(formats)
        self.assertEqual(d, expected_sizeof)
        self.assertEqual(_struct.calcsize("x"), 1)
        for formatchar in formats:
            s = _struct.Struct(formatchar)
            self.assertEqual(s.format, formatchar)
            self.assertEqual(s.size, _struct.calcsize(formatchar))
            self.assertEqual(s.alignment, _struct.calcsize(formatchar))
        s = _struct.Struct(formats)
        self.assertEqual(s.format, formats)
        self.assertEqual(s.size, expected_sizeof)

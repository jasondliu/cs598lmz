import _struct
# Test _struct.Struct
#
# XXX These tests are a bit lame, but they're a start.

from _struct import *
import unittest
import sys
from test import test_support

class StructTest(unittest.TestCase):

    def test_calcsize(self):
        self.assertEqual(calcsize('hhi'), 6)
        self.assertEqual(calcsize('hh'), 4)
        self.assertEqual(calcsize('h'), 2)
        self.assertEqual(calcsize('h'), 2)
        self.assertEqual(calcsize('i'), 4)
        self.assertEqual(calcsize('l'), 4)
        self.assertEqual(calcsize('q'), 8)
        self.assertEqual(calcsize('HHI'), 6)
        self.assertEqual(calcsize('hhI'), 6)
        self.assertEqual(calcsize('HHHH'), 8)
        self.assertEqual(calcsize('hhiq'), 12)

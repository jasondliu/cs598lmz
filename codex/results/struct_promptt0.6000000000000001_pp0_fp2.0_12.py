import _struct
# Test _struct.Struct class.

import operator, sys
import unittest
from test import test_support

# Issue #4106: check for integer overflow in format string
class StructOverflowTest(unittest.TestCase):
    def test_overflow(self):
        self.assertRaises(struct.error, struct.Struct, 'i' * (sys.maxint//4))

class StructTest(unittest.TestCase):

    def test_basics(self):
        # Ensure that the format string gets stored
        self.assertEqual(_struct.Struct('hq').format, 'hq')
        self.assertEqual(_struct.Struct('hq').size, 10)
        self.assertEqual(_struct.Struct('hq').__doc__,
                         'Compiled struct object')
        self.assertEqual(_struct.Struct('hq').__str__(),
                         'Compiled struct object')

    def test_format_size_checks(self):
        # Ensure that the format string and size are checked
        self.assertRaises(TypeError, _struct.Struct, 0

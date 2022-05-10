import _struct
# Test _struct.Struct on big-endian architectures
import sys
import unittest
from test import support

# Big-endian architectures
big_endian = [('big', '>')]

# Big-endian architectures with 64-bit longs
big_endian_64 = [('big64', '>')]

# Test struct module
class StructTest(unittest.TestCase):
    def test_format_size(self):
        self.assertEqual(_struct.calcsize('B'), 1)
        self.assertEqual(_struct.calcsize('c'), 1)
        self.assertEqual(_struct.calcsize('x'), 1)
        self.assertEqual(_struct.calcsize('s'), 1)
        self.assertEqual(_struct.calcsize('p'), 1)
        self.assertEqual(_struct.calcsize('P'), 1)
        self.assertEqual(_struct.calcsize('b'), 1)
        self.assertEqual(_struct.calcsize('h'), 2)
        self.assertEqual(_struct.cal

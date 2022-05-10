import _struct
# Test _struct.Struct
from test import test_support
import unittest
from weakref import proxy
import sys

if sys.maxsize > 2**32:
    def big_type(code):
        if code == 'q':
            return 'Q'
        elif code == 'l':
            return 'L'
        return code
else:
    big_type = lambda code: code


class StructTest(unittest.TestCase):

    def setUp(self):
        self.s = _struct.Struct('hhl')

    def test_basics(self):
        self.assertEqual(self.s.size, _struct.calcsize('hhl'))
        self.assertEqual(self.s.pack(1, 2, 3), '\x01\x00\x02\x00\x00\x00\x00\x03')
        self.assertEqual(self.s.unpack('\x01\x00\x02\x00\x00\x00\x00\x03'),
                         (1, 2, 3))

    def

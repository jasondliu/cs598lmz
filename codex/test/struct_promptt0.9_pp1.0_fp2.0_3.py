import _struct
# Test _struct.Struct() with pre-computed format strings

# This test mimics one of the uses of the _struct module in the
# standard library's ctypes module (see Lib/ctypes/test/test_structures.py),
# namely for simple structure definitions using predefined format
# strings.

import unittest
from test import support


class StructTest(unittest.TestCase):
    def check_format(self, fmt, raw):
        self.assertEqual(len(fmt), len(raw))
        self.assertEqual(fmt, raw)
        s = _struct.Struct(fmt)
        x = s.unpack(s.pack(0))
        self.assertEqual(x, 0)

    def check_c_format(self, fmt):
        raw = _struct.calcsize(fmt)
        self.check_format(fmt, raw)


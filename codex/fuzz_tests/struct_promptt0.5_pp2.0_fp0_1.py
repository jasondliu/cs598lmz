import _struct
# Test _struct.Struct

import unittest
import sys

from test import support

if not hasattr(sys, 'gettotalrefcount'):
    raise unittest.SkipTest("needs sys.gettotalrefcount()")

# XXX: This test is not exhaustive, but it exercises the code enough to
# catch most silly mistakes.

class StructTestCase(unittest.TestCase):

    def check_sizeof(self, fmt, size):
        self.assertEqual(_struct.calcsize(fmt), size)

    def check_unpack(self, fmt, data, expected):
        self.assertEqual(_struct.unpack(fmt, data), expected)

    def check_pack(self, fmt, args, expected):
        self.assertEqual(_struct.pack(fmt, *args), expected)

    def check_pack_into(self, fmt, args, expected, offset=0):
        buf = bytearray(expected)
        _struct.pack_into(fmt, buf, offset, *args)
        self.assertEqual(buf, expected)

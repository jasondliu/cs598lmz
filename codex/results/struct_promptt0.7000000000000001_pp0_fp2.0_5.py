import _struct
# Test _struct.Struct() arguments

import struct
from test import support
from test.support import bigmemtest
import unittest

from test import mapping_tests

class StructTest(unittest.TestCase):

    def assertIsSubclass(self, obj, cls, msg=None):
        self.assertTrue(issubclass(obj, cls), msg)

    def test_struct_error(self):
        self.assertIsSubclass(struct.error, Exception)

    def test_struct_unpack_from(self):
        # SF bug #1176284: segfault in unpack_from
        def unpack_from_bug(fmt, buf, offset=0):
            return struct.unpack_from(fmt, buffer(buf), offset)

        self.assertEqual(unpack_from_bug('=i', '\x00'*4), (0,))
        self.assertEqual(unpack_from_bug('=i', '\x00'*5, 1), (0,))
        self.assertRaises(struct.error, unpack

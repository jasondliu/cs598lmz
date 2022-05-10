import _struct
# Test _struct.Struct.
#
# _struct.Struct(...) returns a type, not an instance.
#
# XXX: These test_struct tests are not fully independent of each other.
# XXX: Some might fail, but that doesn't mean the feature is broken.
# For example, some tests will fail if the underlying platform doesn't
# support a particular format.  That's OK.  Others tests might fail
# if the underlying platform's 'long long' is different from ours.
# That's also OK.  Some tests will only fail if the underlying
# machine has different endianness.  That's OK too.
#
# This module also tests big-endian and little-endian variants of
# the native formats.

import unittest
import _testcapi
import sys
import struct

class StructTest(unittest.TestCase):
    def test_format_size_alignment(self):
        for format in 'bBhHiIlLqQ':
            s = struct.Struct(format)
            self.assertEqual(s.size, struct.calcsize(format))
            self.assertE

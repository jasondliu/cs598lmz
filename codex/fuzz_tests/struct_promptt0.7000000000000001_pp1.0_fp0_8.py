import _struct
# Test _struct.Struct for little-endian long long and unsigned long long.
# Both are supported on all platforms
#
# XXX: Currently, these tests are not run by default.  The test suite
# should be able to test these functions on all platforms, so that
# they can be enabled by default.

import unittest

from test import test_support

class LLongTest(unittest.TestCase):

    def test_int(self):
        # Verify packing and unpacking with various long and int objects.
        s = _struct.Struct('<Q')
        for i in [0, 1, -1, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF, 0xFFFFFFFFFFFFFFFF]:
            self.assertEqual(s.unpack(s.pack(i)), (i,))
        for i in [0, 1, -1, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF]:
            self.assertEqual(s.unpack(s.pack(long(i))), (i,))
        for i in [0, 1, -1

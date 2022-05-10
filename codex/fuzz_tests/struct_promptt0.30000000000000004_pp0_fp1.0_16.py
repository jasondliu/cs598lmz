import _struct
# Test _struct.Struct.

import struct
import sys
import test.support
import unittest

# _struct.Struct is a wrapper for the built-in struct module.
# It is used to create new classes that are like the built-in classes,
# but support other formats.

# The following tests are adapted from the tests for the built-in struct module.

class StructTest(unittest.TestCase):

    # This test is copied from the test_struct.py test_unpack_from.
    def test_unpack_from(self):
        # Test unpack_from()
        s = _struct.Struct('hhl')
        buf = bytes(range(1, 9))
        self.assertEqual(s.unpack_from(buf, 0), (1, 2, 3))
        self.assertEqual(s.unpack_from(buf, 2), (3, 4, 5))
        self.assertEqual(s.unpack_from(buf, 4), (5, 6, 7))
        self.assertEqual(s.unpack_from(buf, 6),

import _struct
# Test _struct.Struct

import struct
import sys
import unittest

from test import support

class StructTest(unittest.TestCase):

    def test_format(self):
        # Make sure we can use the format string in the constructor
        # and in pack/unpack/calcsize.
        s = _struct.Struct('hhh')
        self.assertEqual(s.size, 6)
        self.assertEqual(s.pack(1, 2, 3), b'\x01\x00\x02\x00\x03\x00')
        self.assertEqual(s.unpack(b'\x01\x00\x02\x00\x03\x00'), (1, 2, 3))
        self.assertEqual(s.calcsize(b'\x01\x00\x02\x00\x03\x00'), 6)

        # Check that we can use the format string more than once
        s = _struct.Struct('hhh')
        self.assertEqual(s.size, 6)
        self.assertEqual

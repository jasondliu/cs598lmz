import _struct
# Test _struct.Struct
#
# This tests the _struct module.
#
# The test cases are taken from the Python 2.7.3 documentation.
#
# The test cases are run with different endianness, and different
# alignment.

import struct
import unittest

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Test the _struct module.
        #
        # The test cases are taken from the Python 2.7.3 documentation.
        #
        # The test cases are run with different endianness, and different
        # alignment.

        for endian in '<>!':
            for align in range(8):
                fmt = endian + '%d' % align
                print(fmt)
                s = struct.Struct(fmt)
                self.assertEqual(s.size, align)
                self.assertEqual(s.pack(42), b'\x2a' * align)
                self.assertEqual(s.unpack(b'\x2a' * align), (42,))

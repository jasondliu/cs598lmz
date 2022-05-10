import _struct
# Test _struct.Struct by comparing it to the standard struct module.

import struct
import unittest

class StructTestCase(unittest.TestCase):
    def test_format_size(self):
        for format in ['x', 'c', 'b', 'B', '?',
                       'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q',
                       'f', 'd', 's', 'p']:
            self.assertEqual(struct.calcsize(format), _struct.calcsize(format))

    def test_unpack(self):
        for format in ['x', 'c', 'b', 'B', '?',
                       'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q',
                       'f', 'd', 's', 'p']:
            for bigendian in (False, True):
                for size in range(1, 33):
                    s = struct.Struct(format)
                    b = s.pack(*range(size))

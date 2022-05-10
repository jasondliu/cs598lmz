import _struct
# Test _struct.Struct

import unittest
import sys
import struct

from test import support

# Some of these tests are also in test_struct.  This is intentional.

class StructTest(unittest.TestCase):

    def test_struct(self):
        # Make sure we can create a Struct object
        s = _struct.Struct('i')
        self.assertEqual(s.size, struct.calcsize('i'))
        self.assertEqual(s.format, 'i')
        self.assertRaises(TypeError, _struct.Struct, 'i', 'i')

    def test_unpack(self):
        # Make sure we can unpack things correctly
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'\0\0\0\0'), (0,))
        self.assertEqual(s.unpack(b'\1\0\0\0'), (1,))
        self.assertEqual(s.unpack(b'\1\0\0\0junk'), (1,

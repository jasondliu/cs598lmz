import _struct
# Test _struct.Struct

import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_unpack_from(self):
        # Issue #17097: struct.unpack_from() should accept a buffer object
        # as input.
        s = _struct.Struct('i')
        buf = memoryview(b'xxxxxx\x01\x00\x00\x00')
        self.assertEqual(s.unpack_from(buf, offset=4), (1,))
        self.assertEqual(s.unpack_from(buf, offset=4, size=4), (1,))
        self.assertEqual(s.unpack_from(buf, offset=4, size=8), (1,))
        self.assertRaises(ValueError, s.unpack_from, buf, offset=4, size=3)
        self.assertRaises(ValueError, s.unpack_from, buf, offset=4, size=5)
        self.assertRaises(ValueError, s.unpack_

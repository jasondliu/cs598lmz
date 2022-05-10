import _struct
# Test _struct.Struct

import sys
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_struct_without_format(self):
        # Issue #1797703
        self.assertRaises(TypeError, _struct.Struct)

    def test_unpack_from(self):
        import array
        s = _struct.Struct('i')
        buf = array.array('b', [0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0])
        offset = 0
        self.assertEqual(s.unpack_from(buf, offset), (0,))
        offset += s.size
        self.assertEqual(s.unpack_from(buf, offset), (1,))
        offset += s.size
        self.assertEqual(s.unpack_from(buf, offset), (2,))
        offset += s.size
        self.assertEqual(offset, len(buf))
        self.assertRaises(struct.error, s.unpack_from, buf

import _struct
# Test _struct.Struct

import random
import unittest
from test import support

class StructTestCase(unittest.TestCase):

    def test_ctor(self):
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.size, 4)
        self.assertRaises(TypeError, _struct.Struct, 1, 2, 3)

    def test_unpack_from(self):
        s = _struct.Struct('i')
        buf = _struct.pack('i', 42)
        self.assertEqual(s.unpack_from(buf), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s.unpack_from(memoryview(buf), 0), (42,))
        # these should all raise
        self.assertRaises(TypeError, s.unpack_from)
        self

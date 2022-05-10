import _struct
# Test _struct.Struct
from test import test_support
import unittest
from cStringIO import StringIO

# The tests here apply to all struct formats, not just native ones.

class StructTest(unittest.TestCase):
    def test_unpack_from(self):
        s = _struct.Struct('i')
        st = memoryview(s.pack(1)).cast('b')
        self.assertEqual(s.unpack_from(st), (1,))
        self.assertEqual(s.unpack_from(st, 0), (1,))
        self.assertEqual(s.unpack_from(st, 1), (0,))
        self.assertRaises(struct.error, s.unpack_from, st, 2)
        self.assertRaises(struct.error, s.unpack_from, st, -1)

    def test_unpack_from_buffer(self):
        s = _struct.Struct('i')
        st = buffer(s.pack(1))
        self.assertEqual(s.unpack_from(

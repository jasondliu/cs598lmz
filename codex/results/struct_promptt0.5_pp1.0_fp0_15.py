import _struct
# Test _struct.Struct.unpack_from
from test import test_support
import unittest

class StructTest(unittest.TestCase):
    def test_unpack_from(self):
        s = _struct.Struct('i')
        buf = buffer(s.pack(42))
        self.assertEqual(s.unpack_from(buf), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s.unpack_from(buf, 0), (42,))
        self.assertEqual(s

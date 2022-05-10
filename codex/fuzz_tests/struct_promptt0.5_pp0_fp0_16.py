import _struct
# Test _struct.Struct()
from test import support
import unittest


class StructTestCase(unittest.TestCase):
    def test_struct_unpack_from(self):
        # Test that _struct.Struct.unpack_from() accepts a buffer and offset.
        s = _struct.Struct('i')
        buf = bytes(range(16))
        self.assertEqual(s.unpack_from(buf, 4), (4,))
        self.assertEqual(s.unpack_from(buf, 8), (8,))
        self.assertEqual(s.unpack_from(memoryview(buf), 12), (12,))

    def test_struct_unpack_from_empty_buffer(self):
        # Issue #14591: unpack_from should fail if the buffer is empty
        s = _struct.Struct('i')
        self.assertRaises(ValueError, s.unpack_from, b'', 0)

    def test_struct_unpack_from_buffer_too_short(self):
        # Issue #14591: unpack_from

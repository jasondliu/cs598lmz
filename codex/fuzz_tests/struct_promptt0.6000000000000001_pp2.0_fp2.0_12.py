import _struct
# Test _struct.Struct .pack_into()

from test.support import run_unittest
import unittest

from io import BytesIO


class StructTest(unittest.TestCase):

    def test_pack_into(self):
        buffer = bytearray(b'\0' * 10)
        fmt = 'hhh'
        struct_ = _struct.Struct(fmt)
        struct_.pack_into(buffer, 2, 1, 2, 3)
        self.assertEqual(buffer, b'\0\0\0\1\0\2\0\3\0\0')

    def test_pack_into_with_offset_out_of_range(self):
        buffer = bytearray(b'\0' * 10)
        fmt = 'hhh'
        struct_ = _struct.Struct(fmt)
        self.assertRaises(ValueError, struct_.pack_into, buffer, 10, 1, 2, 3)

    def test_pack_into_with_buffer_too_short(self):
        buffer = bytearray(b

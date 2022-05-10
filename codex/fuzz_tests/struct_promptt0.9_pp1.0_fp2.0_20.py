import _struct
# Test _struct.Struct.
import struct
import io
import sys

class FunctionsTestCase:

    def test_create_string_buffer(self):
        buf = _struct.create_string_buffer(10)
        buf.raw = b'0123456789'
        self.assertEqual(len(buf), 10)
        self.assertEqual(buf[5], 53)

    def test_get_size(self):
        self.assertEqual(_struct.calcsize(b'i'), _struct.calcsize(struct.Struct('i')))
        self.assertEqual(_struct.calcsize(b'i'), struct.calcsize(b'i'))

    def test_pack(self):
        buf = _struct.pack(b'i', 334)
        buf2 = struct.pack(b'i', 334)
        self.assertEqual(buf, buf2)
        self.assert_(isinstance(buf, bytes))

    def test_unpack(self):
        buf = _struct.pack(b'i', 334)
        val, = _struct

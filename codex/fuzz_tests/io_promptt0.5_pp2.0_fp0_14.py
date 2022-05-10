import io
# Test io.RawIOBase.readinto()

import _io
import test.support
import unittest


class TestRawIO(unittest.TestCase):

    def test_readinto_return_type(self):
        # Issue #16280: readinto() must return an int.
        f = _io.BytesIO(b"abc")
        buf = bytearray(10)
        self.assertIsInstance(f.readinto(buf), int)
        f = _io.StringIO("abc")
        buf = bytearray(10)
        self.assertIsInstance(f.readinto(buf), int)

    def test_readinto_resize(self):
        # Issue #16280: readinto() must not resize the target buffer.
        f = _io.BytesIO(b"abc")
        buf = bytearray(10)
        f.readinto(buf)
        self.assertEqual(len(buf), 10)
        f = _io.StringIO("abc")
        buf = bytearray(10)
        f.readinto(buf

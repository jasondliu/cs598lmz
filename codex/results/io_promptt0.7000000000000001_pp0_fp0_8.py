import io
# Test io.RawIOBase

import _io
from test.support import run_unittest


class ReadTest(unittest.TestCase):

    def test_read_all(self):
        f = _io.BytesIO(b"abcde")
        self.assertEqual(f.read(), b"abcde")

    def test_read_0(self):
        f = _io.BytesIO(b"abcde")
        self.assertEqual(f.read(0), b"")

    def test_read_1(self):
        f = _io.BytesIO(b"abcde")
        self.assertEqual(f.read(1), b"a")

    def test_read_3(self):
        f = _io.BytesIO(b"abcde")
        self.assertEqual(f.read(3), b"abc")

    def test_read_all_to_buffer(self):
        f = _io.BytesIO(b"abcde")
        buf = bytearray(5)
        self.assertEqual(f.read

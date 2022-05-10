import io
# Test io.RawIOBase.readinto() method

import _io

class TestReadintoRawIO(unittest.TestCase):
    def test_readinto_simple(self):
        b = bytearray(b"abc")
        f = io.BytesIO(b)
        n = f.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"abc")

    def test_readinto_simple_0(self):
        b = bytearray(b"abc")
        f = io.BytesIO(b)
        n = f.readinto(b, 0, 0)
        self.assertEqual(n, 0)
        self.assertEqual(b, b"abc")

    def test_readinto_simple_1(self):
        b = bytearray(b"abc")
        f = io.BytesIO(b)
        n = f.readinto(b, 1, 0)
        self.assertEqual(n, 0)
        self.assertEqual(b, b"

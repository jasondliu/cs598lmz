import io
# Test io.RawIOBase

import _io

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        b = io.BytesIO(b"abc")
        self.assertEqual(b.read(), b"abc")
        self.assertEqual(b.read(), b"")

    def test_readall(self):
        # Test RawIOBase.readall()
        b = io.BytesIO(b"abc")
        self.assertEqual(b.readall(), b"abc")
        self.assertEqual(b.readall(), b"")

    def test_readinto(self):
        # Test RawIOBase.readinto()
        b = io.BytesIO(b"abc")
        buf = bytearray(2)
        self.assertEqual(b.readinto(buf), 2)
        self.assertEqual(buf, b"ab")
        self.assertEqual(b.readinto(buf), 1)
        self.assertEqual(buf, b"

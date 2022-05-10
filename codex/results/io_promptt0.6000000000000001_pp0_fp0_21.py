import io
# Test io.RawIOBase

import _io

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(_io.RawIOBase):
            def read(self, n=-1):
                return b"xyz"
        rawio = TestRawIO()
        self.assertEqual(rawio.read(2), b"xy")
        self.assertEqual(rawio.read(2), b"z")
        self.assertEqual(rawio.read(2), b"")

    def test_readinto(self):
        # Test RawIOBase.readinto()
        class TestRawIO(_io.RawIOBase):
            def readinto(self, b):
                b[:3] = b"xyz"
                return 3
        rawio = TestRawIO()
        b = bytearray(5)
        n = rawio.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"xyz

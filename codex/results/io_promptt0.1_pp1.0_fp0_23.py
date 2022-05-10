import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test that self.read() calls self.readinto()
        class TestRawIO(io.RawIOBase):
            def readinto(self, b):
                b[:] = b"foo"
                return 3
        f = TestRawIO()
        self.assertEqual(f.read(5), b"foo")
        self.assertEqual(f.read(5), b"")

    def test_readall(self):
        # Test that self.readall() calls self.read()
        class TestRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b"foo"
        f = TestRawIO()
        self.assertEqual(f.readall(), b"foo")

    def test_readinto(self):
        # Test that self.readinto() calls self.read()
        class TestRawIO(io.RawIOBase):
            def read(self

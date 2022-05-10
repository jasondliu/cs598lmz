import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import bigmemtest

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                b[:3] = b"foo"
                return 3
        buf = bytearray(5)
        f = TestRawIO()
        n = f.readinto(buf)
        self.assertEqual(n, 3)
        self.assertEqual(buf, b"foob\x00")
        self.assertEqual(f.readinto(buf), 0)
        self.assertRaises(TypeError, f.readinto, memoryview(buf))

    def test_readall(self):
        # Test RawIOBase.readall()
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self,

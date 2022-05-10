import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOBaseTestCase(unittest.TestCase):

    def test_abc(self):
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase))

    def test_readinto(self):
        class TestRawIO(io.RawIOBase):
            def __init__(self):
                self.readinto_calls = 0
                self.read_calls = 0
            def readable(self):
                return True
            def read(self, n=-1):
                self.read_calls += 1
                return b'x'
            def readinto(self, b):
                self.readinto_calls += 1
                b[:] = b'x'
                return len(b)

        rawio = TestRawIO()
        b = bytearray(5)
        n = rawio.readinto(b)
        self.assertEqual(n, 5)
        self.assertEqual(b, b'xxxxx')
        self.assertEqual(

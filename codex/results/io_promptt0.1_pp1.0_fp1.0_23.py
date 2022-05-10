import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_calls += 1
                return 0
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        self.assertEqual(rawio.read(), b'')
        self.assertEqual(rawio.readinto_calls, 1)
        self.assertEqual(rawio.read(10), b'')
        self.assertEqual(rawio.readinto_calls, 2)
        self.assertEqual(rawio.read(-1), b'')
        self.assertEqual(rawio.readinto_calls, 3)

    def test_readinto(self):
        # Test RawIOBase.readinto()
        class TestRaw

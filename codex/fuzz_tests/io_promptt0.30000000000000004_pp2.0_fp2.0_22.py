import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test that self.read() returns an empty bytes object on EOF.
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_calls += 1
                return 0
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        self.assertEqual(rawio.read(), b'')
        self.assertEqual(rawio.readinto_calls, 1)

    def test_read1(self):
        # Test that self.read1() returns an empty bytes object on EOF.
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto1(self, b):
                self.readinto1_calls += 1
                return 0
        rawio = TestRawIO()
        rawio.readinto1

import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test that read() returns an empty bytes object on EOF
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                self.readinto_calls += 1
                return 0
        rawio = TestRawIO()
        rawio.readinto_calls = 0
        self.assertEqual(rawio.read(), b'')
        self.assertEqual(rawio.readinto_calls, 1)

    def test_read_non_empty(self):
        # Test that read() returns a non-empty bytes object
        class TestRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                self.readinto_calls += 1
                buf[:] = b'x' * len(buf)
                return len(buf)
        rawio = Test

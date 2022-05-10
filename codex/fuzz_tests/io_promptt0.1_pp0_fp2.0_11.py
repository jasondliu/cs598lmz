import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import bigmemtest

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def __init__(self, test_string):
                self._string_io = io.StringIO(test_string)
            def readinto(self, b):
                return self._string_io.readinto(b)
        buf = bytearray(b' ' * 10)
        buf2 = bytearray(b' ' * 10)
        f = TestRawIO(b"abcdefghij")
        self.assertEqual(f.readinto(buf), 10)
        self.assertEqual(buf, b"abcdefghij")
        self.assertEqual(f.readinto(buf2), 0)
        self.assertEqual(buf2, b" " * 10)
        self.assertEqual(f.readinto(buf2), 0)


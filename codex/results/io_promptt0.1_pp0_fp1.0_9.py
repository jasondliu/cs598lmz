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
        b = bytearray(b'x' * 10)
        r = TestRawIO(b'abcdefghij')
        n = r.readinto(b)
        self.assertEqual(n, 10)
        self.assertEqual(b, b'abcdefghij')
        self.assertEqual(r.readinto(b), 0)
        self.assertRaises(TypeError, r.readinto, memoryview(b'x' * 10))

    def test_readall(self):
        # Test RawIOBase.readall

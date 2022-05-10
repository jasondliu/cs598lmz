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
            def read(self, n=-1):
                return self._string_io.read(n)
            def readable(self):
                return True
        test_string = "ABCDE"
        r = TestRawIO(test_string)
        self.assertEqual(r.read(3), "ABC")
        self.assertEqual(r.read(2), "DE")
        self.assertEqual(r.read(), "")

    def test_readinto(self):
        # Test RawIOBase.readinto()
        class TestRawIO(io.RawIOBase):
            def __init__(self, test_string):
                self._string_

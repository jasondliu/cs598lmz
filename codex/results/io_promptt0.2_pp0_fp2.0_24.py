import io
# Test io.RawIOBase

import unittest
from test import support

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
        test_string = 'abcdefghijklmnopqrstuvwxyz'
        r = TestRawIO(test_string)
        self.assertEqual(r.read(10), test_string[:10])
        self.assertEqual(r.read(10), test_string[10:20])
        self.assertEqual(r.read(10), test_string[20:])
        self.assertEqual(r.read(10), '')
        self.assertEqual(r.read(), '')
        self.

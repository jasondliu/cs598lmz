import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def __init__(self, test_string):
                self._string = test_string
                self._len = len(test_string)
                self._pos = 0
            def read(self, n=-1):
                newpos = min(self._len, self._pos+n)
                r = self._string[self._pos:newpos]
                self._pos = newpos
                return r
        s = 'abcdefghijklmnop'
        f = TestRawIO(s)
        self.assertEqual(f.read(5), 'abcde')
        self.assertEqual(f.read(5), 'fghij')
        self.assertEqual(f.read(5), 'klmno')
        self.assertEqual(f.read(5), 'p')
        self.assert

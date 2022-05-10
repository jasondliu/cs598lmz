import io
# Test io.RawIOBase.readall, which reads from the start.

import _io
import io
import unittest

from test.support import captured_stderr

class ReadallTest(unittest.TestCase):

    def setUp(self):
        self.data = b'abcde'
        self.rawio = _io.BytesIO(self.data)

    def test_readall(self):
        self.assertEqual(self.rawio.readall(), b'abcde')

    def test_read(self):
        self.assertEqual(self.rawio.read(0), b'')
        self.assertEqual(self.rawio.read(1), b'a')
        self.assertEqual(self.rawio.read(2), b'bc')
        self.assertEqual(self.rawio.read(-1), b'de')
        self.assertEqual(self.rawio.read(-1), b'')
        self.assertEqual(self.rawio.read(0), b'')
        self.rawio.

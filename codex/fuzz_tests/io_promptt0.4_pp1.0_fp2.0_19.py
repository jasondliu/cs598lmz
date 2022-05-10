import io
# Test io.RawIOBase

import unittest
import io
from test import support
from test.support import bigmemtest

# Some tests require a file with at least 256 bytes.
MIN_LARGE_FILE_SIZE = 256

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = io.BytesIO()

    def tearDown(self):
        if self.f:
            self.f.close()
        self.f = None

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, b'')

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.f.write, b'')

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.f.seek, 0)

    def test_tell(self):
        self.assertRaises

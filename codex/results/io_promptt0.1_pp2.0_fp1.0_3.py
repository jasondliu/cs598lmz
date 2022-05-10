import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase

class TestRawIO(RawIOBase):

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        return 0

    def write(self, b):
        return 0

    def seek(self, pos, whence=0):
        return 0

    def tell(self):
        return 0

    def close(self):
        pass

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        rawio = TestRawIO()
        self.assertTrue(rawio.readable())
        self.assertTrue(rawio.writable())
        self.assertTrue(rawio.seekable())
        self.assertEqual(rawio.readinto(b''), 0)
        self.assertEqual(rawio.write(b''), 0)
        self.assertEqual(rawio.seek(0), 0)

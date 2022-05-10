import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import TESTFN, unlink

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = io.BytesIO()

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.f.write, b"")

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.f.seek, 0)

    def test_tell(self):
        self.assertRaises(io.UnsupportedOperation, self.f.tell)

    def test_truncate(self):
        self.assertRaises(io.UnsupportedOperation, self.f.truncate)

    def test_fileno(self

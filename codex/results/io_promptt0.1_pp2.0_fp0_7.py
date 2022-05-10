import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import TESTFN, unlink

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'wb')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.f.write, b"blah")

    def test_close(self):
        self.f.close()
        self.f = None

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, self.f.fileno)

    def test_isatty(

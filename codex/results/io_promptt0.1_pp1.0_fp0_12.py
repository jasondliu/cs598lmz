import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import TESTFN, unlink

class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = io.RawIOBase()

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, b'')

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.f.write, b'')

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, self.f.fileno)

    def test_isatty(self):
        self.assertEqual(self.f.isatty(), False)

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.f.seek, 0)

    def test_tell(self):
        self

import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read_write(self):
        # Test read() and write()
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)
        self.assertRaises(io.UnsupportedOperation, f.read, 10)
        self.assertRaises(io.UnsupportedOperation, f.write, b"")
        self.assertRaises(io.UnsupportedOperation, f.write, b"xyzzy")

    def test_fileno(self):
        # Test fileno()
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.fileno)

    def test_isatty(self):
        # Test isatty()
        f = io.RawIOBase()
        self.assertEqual(f.isatty(), False)

    def test_readinto(self):
        # Test readinto()
        f = io.RawIOBase

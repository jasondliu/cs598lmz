import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Read should return an empty bytes object at EOF
        rawio = RawIOBase()
        self.assertEqual(rawio.read(1), b'')

    def test_readall(self):
        # Readall should return an empty bytes object at EOF
        rawio = RawIOBase()
        self.assertEqual(rawio.readall(), b'')

    def test_readinto(self):
        # Readinto should return 0 at EOF
        rawio = RawIOBase()
        b = bytearray(1)
        self.assertEqual(rawio.readinto(b), 0)

    def test_readinto_resize(self):
        # Readinto should not resize the buffer it's given
        rawio = RawIOBase()
        b = bytearray(1)
        self.assertRaises(BufferError, rawio.readinto, b

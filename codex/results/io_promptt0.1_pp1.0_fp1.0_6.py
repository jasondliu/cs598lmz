import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Read method
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read, 0)

    def test_readinto(self):
        # Readinto method
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray(1))

    def test_write(self):
        # Write method
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'1')

    def test_close(self):
        # Close method
       

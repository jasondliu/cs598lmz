import io
# Test io.RawIOBase
import random
import unittest
from test import support
import _pyio as pyio

class BaseTestRawIO(object):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.read)
        self.assertRaises(io.UnsupportedOperation, self.IO.read, 0)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, self.IO.readinto, bytearray(1))

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.write, b'')
        self.assertRaises(io.UnsupportedOperation, self.IO.write, b'1')

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.seek, 0)

    def test_tell(self):
        self.assertRaises(io.UnsupportedOperation

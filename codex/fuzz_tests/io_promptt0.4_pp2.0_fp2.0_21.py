import io
# Test io.RawIOBase

import _io
import unittest
import weakref
from test import support

# Base class for defining tests.
class BaseRawIOTest:
    # Subclasses should override
    def new_io(self, *args):
        raise NotImplementedError

    def test_raw_read(self):
        io = self.new_io()
        self.assertRaises(io.UnsupportedOperation, io.read)

    def test_raw_readinto(self):
        io = self.new_io()
        self.assertRaises(io.UnsupportedOperation, io.readinto, bytearray(b'x'))

    def test_raw_write(self):
        io = self.new_io()
        self.assertRaises(io.UnsupportedOperation, io.write, b'x')

    def test_raw_fileno(self):
        io = self.new_io()
        self.assertRaises(io.UnsupportedOperation, io.fileno)

    def test_raw_seek(self):
        io = self.new

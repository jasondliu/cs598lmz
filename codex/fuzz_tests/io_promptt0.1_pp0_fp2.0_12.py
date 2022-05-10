import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# Base class for testing io.RawIOBase.
# The tests are performed both in blocking and non-blocking mode.
#
# Subclasses must override read(), readinto() and write().
#
# The io object is always non-seekable.
class RawIOTest:

    def setUp(self):
        self.iobase = io.RawIOBase()
        self.iobase.__init__(self)

    def tearDown(self):
        self.iobase.close()

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.iobase.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.iobase.readinto, bytearray(1))

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, self.iobase.readall)

    def test_write(self):
        self

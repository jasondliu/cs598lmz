import io
# Test io.RawIOBase

import io
import os
import sys
import tempfile
import unittest
from test import support

# XXX This should probably be moved to the io module tests, but currently
# the io module does not contain much unittest support.

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # .read() returns bytes
        io_obj = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, io_obj.read)

    def test_readinto(self):
        # .readinto() writes into the buffer
        io_obj = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, io_obj.readinto, bytearray())

    def test_readall(self):
        # .readall() returns bytes
        io_obj = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, io_obj.readall)

    def test_write(self):
        # .write() accepts bytes
        io_obj = io.

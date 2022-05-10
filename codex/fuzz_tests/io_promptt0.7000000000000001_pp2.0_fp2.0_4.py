import io
# Test io.RawIOBase

import threading
import unittest
from test import support

class RawIOBaseTestCase(unittest.TestCase):

    def test_read(self):
        with support.check_warnings():
            self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read, 0)

    def test_write(self):
        with support.check_warnings():
            self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')

    def test_readinto(self):
        with support.check_warnings():
            self.assertRaises(io.UnsupportedOperation,
                              io.RawIOBase().readinto, bytearray())

    def test_readall(self):
        with support.check_warnings():
            self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readall)

    def test_close(self):
        with support.check_warnings():
            io.RawIOBase().close()

    def test_seek(self):
        with support.

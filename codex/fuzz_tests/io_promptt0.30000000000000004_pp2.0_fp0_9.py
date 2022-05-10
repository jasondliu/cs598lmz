import io
# Test io.RawIOBase
# io.RawIOBase.readinto
# io.RawIOBase.write
# io.RawIOBase.fileno

import sys
import unittest
from test import support
from test.support import os_helper

class RawIOTest(unittest.TestCase):

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write,
                          b"")

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().fileno)

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readall)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readline(self):
       

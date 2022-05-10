import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import os_helper
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRandom
from io import DEFAULT_BUFFER_SIZE

class BaseTestRawIO(object):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.readinto, bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.write, b'')

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.fileno)

    def test_isatty(self):
        self.assertFalse(self.IO.isatty())

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, self.IO.seek, 0)

    def test_tell(self):

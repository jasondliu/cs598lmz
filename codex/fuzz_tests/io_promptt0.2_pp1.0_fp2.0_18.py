import io
# Test io.RawIOBase

import unittest
from test import support
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRWPair, BufferedRandom
from io import DEFAULT_BUFFER_SIZE
from io import UnsupportedOperation

class BaseTestRawIO(object):

    def test_read(self):
        self.assertRaises(UnsupportedOperation, self.IO.read)

    def test_readinto(self):
        self.assertRaises(UnsupportedOperation, self.IO.readinto, bytearray())

    def test_write(self):
        self.assertRaises(UnsupportedOperation, self.IO.write, b'')

    def test_fileno(self):
        self.assertRaises(UnsupportedOperation, self.IO.fileno)

    def test_isatty(self):
        self.assertRaises(UnsupportedOperation, self.IO.isatty)

    def test_seek(self):
        self.assertRaises(UnsupportedOperation, self.IO.seek, 0)

    def test_tell(self):
       

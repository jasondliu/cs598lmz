import io
# Test io.RawIOBase

import unittest
from test import test_support

import io

class RawIOTest(unittest.TestCase):

    def test_args(self):
        # No args
        self.assertRaises(TypeError, io.RawIOBase)
        # Too many args
        self.assertRaises(TypeError, io.RawIOBase, None, None)

class TestRawIO(io.RawIOBase):
    def __init__(self, test_case, buf=''):
        self._test_case = test_case
        self._buffer = io.BytesIO(buf)

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        return self._buffer.seek(pos, whence)

    def readinto(self, b):
        return self._buffer.readinto(b)

    def write(self, b):
        return self._buffer.write(b)

    def readall(self):

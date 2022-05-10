import io
# Test io.RawIOBase.readinto

# This is a base class test case that is meant to be called from
# test_io.py

import io
import unittest
from test import support

class BaseBytesRawIO(io.RawIOBase):
    def __init__(self, initial_bytes=b''):
        self._bytes = initial_bytes

    def readinto(self, buf):
        n = len(buf)
        if n > len(self._bytes):
            n = len(self._bytes)
        buf[:n] = self._bytes[:n]
        self._bytes = self._bytes[n:]
        return n

    def write(self, buf):
        self._bytes += buf
        return len(buf)

class BaseTestRawIO(unittest.TestCase):
    def setUp(self):
        self.iobuf = b'abcdefghij'
        self.iobufsize = len(self.iobuf)
        self.bigbuf = b'x' * (support.PIPE_MAX_SIZE * 4)
       

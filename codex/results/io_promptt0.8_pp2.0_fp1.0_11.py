import io
# Test io.RawIOBase-compatible class.

import unittest
import os
import os.path
import tempfile
import weakref

# The test relies on this specific structure of readinto(), as well as some
# inner workings of the io module.

class MyIO(io.RawIOBase):

    def __init__(self, initial_value=b""):
        self.buf = initial_value

    def readinto(self, b):
        n = len(b)
        result = self._read(n)
        b[:len(result)] = result
        return len(result)

    def _read(self, n=-1):
        if n is None or n < 0:
            result = self.buf
            self.buf = b""
        else:
            result = self.buf[:n]
            self.buf = self.buf[n:]

        self.pos = len(self.buf)
        return result

    def write(self, b):
        self.buf += b
        self.pos = len(self.buf)
        return len(b)

    def

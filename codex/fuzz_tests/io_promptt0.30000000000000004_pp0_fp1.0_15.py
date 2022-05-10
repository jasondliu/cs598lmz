import io
# Test io.RawIOBase.readinto

import io
import os
import sys
import unittest
from test import support

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self._buf = buf
        self._pos = 0

    def readinto(self, b):
        n = len(b)
        if self._pos >= len(self._buf):
            return None
        if n > len(self._buf) - self._pos:
            n = len(self._buf) - self._pos
        b[:n] = self._buf[self._pos:self._pos+n]
        self._pos += n
        return n

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            newpos = pos
        elif whence == 1:
            newpos = self._pos + pos
        elif whence == 2:
            newpos = len(self._buf) + pos
        else:
            raise Value

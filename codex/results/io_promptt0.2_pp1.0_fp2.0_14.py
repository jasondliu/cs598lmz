import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support

# Test RawIOBase using a StringIO object

class TestRawIO(io.RawIOBase):

    def __init__(self, buf=b''):
        self._buf = buf
        self._pos = 0

    def read(self, n=-1):
        if n >= 0:
            newpos = min(self._pos + n, len(self._buf))
            b = self._buf[self._pos:newpos]
            self._pos = newpos
            return b
        else:
            newpos = len(self._buf)
            b = self._buf[self._pos:]
            self._pos = newpos
            return b

    def write(self, b):
        newpos = self._pos + len(b)
        if newpos > len(self._buf):
            self._buf += b'\x00' * (newpos - len(self._buf))
        self._buf = self._buf[:self._pos] + b + self._buf[

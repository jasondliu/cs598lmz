import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import os_helper

# Test RawIOBase using a StringIO object

class TestRawIO(io.RawIOBase):

    def __init__(self, buf=b''):
        self.buf = buf
        self.pos = 0

    def read(self, n=-1):
        if n >= 0:
            newpos = min(self.pos + n, len(self.buf))
            b = self.buf[self.pos:newpos]
            self.pos = newpos
            return b
        else:
            newpos = len(self.buf)
            b = self.buf[self.pos:]
            self.pos = newpos
            return b

    def write(self, b):
        newpos = self.pos + len(b)
        if newpos > len(self.buf):
            self.buf += b'\x00' * (newpos - len(self.buf))
        self.buf = self.buf[:self

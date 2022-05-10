import io
# Test io.RawIOBase.readinto()

import os
import sys
import unittest
from test import support

# Skip this test if the implementation doesn't override RawIOBase.readinto().
if io.RawIOBase.readinto is io.IOBase.readinto:
    raise unittest.SkipTest('RawIOBase.readinto() not implemented')

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def read(self, n=-1):
        if n == -1:
            newpos = len(self.buf)
        else:
            newpos = min(self.pos + n, len(self.buf))
        b = self.buf[self.pos:newpos]
        self.pos = newpos
        return b

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        else:

import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok

# Test RawIOBase using a StringIO object

class TestRawIO(io.RawIOBase):

    def __init__(self, buf=b''):
        self.buf = buf
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        if self.pos >= len(self.buf):
            return 0
        if n > len(self.buf) - self.pos:
            n = len(self.buf) - self.pos
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def write(self, b):
        n = len(b)
        if self.pos > len(self.buf):
            self.buf += b'\x00' * (self.pos - len(self.buf))
        if n > len(self.buf) - self

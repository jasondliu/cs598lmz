import io
# Test io.RawIOBase

import _io
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok
import unittest

# Test RawIOBase using a memory buffer

class MemoryIO(io.RawIOBase):
    def __init__(self, initial_bytes=b''):
        self.buf = bytearray(initial_bytes)
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        if self.closed:
            raise ValueError("read from closed file")
        if self.pos >= len(self.buf):
            return 0
        if n > len(self.buf) - self.pos:
            n = len(self.buf) - self.pos
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def write(self, b):
        if self.closed:
            raise ValueError("write to closed file")
        n = len(b)
       

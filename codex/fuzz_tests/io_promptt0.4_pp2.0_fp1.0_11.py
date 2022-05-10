import io
# Test io.RawIOBase.readinto()

import io
import os
import sys
import tempfile
import unittest
from test import support

class TestRawIO(io.RawIOBase):

    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def readinto(self, b):
        n = len(self.buf) - self.pos
        if n > len(b):
            n = len(b)
        if n > 0:
            b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def readable(self):
        return True


class TestRawIOBuffer(TestRawIO):

    def readinto(self, b):
        n = len(self.buf) - self.pos
        if n > len(b):
            n = len(b)
        if n > 0:
            b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def readable

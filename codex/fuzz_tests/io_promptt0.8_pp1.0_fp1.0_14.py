import io
# Test io.RawIOBase.readall
# This test is not exhaustive of RawIOBase.readall
# It only tests the success cases

import _io
import unittest

from test import support

# A RawIOBase implementation for testing
class TestRawIO(io.RawIOBase):
    def __init__(self):
        self.pos = 0
        self.content = bytearray(b'abcdef')

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return True

    def readinto(self, b):
        # readinto() should not be called
        raise AssertionError()

    def read(self, n=None):
        if n is None:
            n = len(self.content) - self.pos
        res = self.content[self.pos:self.pos+n]
        self.pos += n
        return bytes(res)

    def readall(self):
        res = self.content[self.pos:]
        self.pos = len(self.content)


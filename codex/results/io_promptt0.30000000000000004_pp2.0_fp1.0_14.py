import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support


class MyRawIO(_io.RawIOBase):

    def __init__(self):
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        for i in range(n):
            b[i] = 65 + self.pos % 26
            self.pos += 1
        return n

    def write(self, b):
        self.pos += len(b)
        return len(b)

    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = 1000 + pos
        else:
            raise ValueError("whence must be 0, 1 or 2")
        return self.pos

    def tell(self):
        return self.pos

    def truncate(self, pos=None):
        if pos is None:
            pos = self.pos


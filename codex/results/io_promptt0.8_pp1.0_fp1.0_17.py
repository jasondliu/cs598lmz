import io
# Test io.RawIOBase implements read, readinto, readall, write,
# seek and tell.
from io import RawIOBase
import os
from os import SEEK_CUR, SEEK_SET, SEEK_END
from io import open
from test.support import unlink


class MyRawIO(RawIOBase):

    def __init__(self, buf):
        self.buf = buf

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        l = len(b)
        if l > len(self.buf):
            l = len(self.buf)
        b[:l] = self.buf[:l]
        self.buf = self.buf[l:]
        return l

    def write(self, b):
        self.buf += b
        return len(b)

    def seek(self, pos, whence=SEEK_SET):
        if whence == SEEK_SET:
            self.buf = self.buf[pos:]


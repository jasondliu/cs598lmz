import io
# Test io.RawIOBase.readinto()

import _io

class TestRawIO(io.RawIOBase):

    def __init__(self, buf):
        self._buf = buf
        self._pos = 0

    def readinto(self, b):
        n = len(self._buf) - self._pos
        if n > len(b):
            n = len(b)
        if n > 0:
            b[:n] = self._buf[self._pos:self._pos+n]
        self._pos += n
        return n

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            self._pos = pos
        elif whence == 1:
            self._pos += pos
        elif whence == 2:
            self._pos = len(self._buf) + pos
        return self._pos

    def tell(self):
        return self._pos

    def readable(self):
        return True

    def writable(self):
        return False


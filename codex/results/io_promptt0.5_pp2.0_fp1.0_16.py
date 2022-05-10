import io
# Test io.RawIOBase
import _io
# Test _io.BufferedIOBase
import _pyio
# Test _pyio.TextIOBase

class MyRawIO(_io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self._tell = 0
    def readinto(self, b):
        n = len(b)
        if self._tell >= len(self.buf):
            return 0
        if n > len(self.buf) - self._tell:
            n = len(self.buf) - self._tell
        b[:n] = self.buf[self._tell:self._tell+n]
        self._tell += n
        return n
    def read(self, n=None):
        if n is None:
            res = self.buf[self._tell:]
            self._tell = len(self.buf)
            return res
        else:
            res = self.buf[self._tell:self._tell+n]
            self._tell += len(res)
            return res
    def write(self, b

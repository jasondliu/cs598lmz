import io
# Test io.RawIOBase.readall()

class MyRawIO(io.RawIOBase):
    def __init__(self, buf):
        self._buf = buf
        self._pos = 0

    def readall(self):
        if self._pos != 0:
            raise RuntimeError("raw readall() should not be called "
                               "after a partial read")
        return self._buf

    def readinto(self, b):
        l = len(b)
        if self._pos + l > len(self._buf):
            l = len(self._buf) - self._pos
        b[:l] = self._buf[self._pos:self._pos+l]
        self._pos += l
        return l

    def readable(self):
        return True

class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self._raw = raw
        self._pos = 0


import io
# Test io.RawIOBase
# Test io.RawIOBase.readinto

class BytesIO(io.RawIOBase):
    def __init__(self, initial_bytes=b""):
        self._buffer = bytearray(initial_bytes)
        self._pos = 0

    def readinto(self, b):
        n = min(len(b), len(self._buffer) - self._pos)
        if n > 0:
            b[:n] = self._buffer[self._pos:self._pos+n]
            self._pos += n
        return n

    def write(self, b):
        n = len(b)
        if n > 0:
            if self._pos == len(self._buffer):
                self._buffer.extend(b)
            else:
                self._buffer[self._pos:self._pos+n] = b
            self._pos += n
        return n

    def seek(self, pos, whence=0):
        if whence == 0:
            self._pos = pos

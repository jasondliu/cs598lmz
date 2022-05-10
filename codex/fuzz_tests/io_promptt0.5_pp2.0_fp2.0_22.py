import io
# Test io.RawIOBase

# io.RawIOBase.readinto()
class BytesIO(io.RawIOBase):
    def __init__(self, initial_bytes=None):
        self._buffer = bytearray(initial_bytes or b'')
        self._pos = 0

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self._pos = offset
        elif whence == io.SEEK_CUR:
            self._pos += offset
        elif whence == io.SEEK_END:
            self._pos = len(self._buffer) + offset
        return self._pos

    def tell(self):
        return self._pos

    def readinto(self, b):
        n = len(b)
        if self._pos + n > len(self._buffer):
            n = len(self._buffer) - self._pos
            b = memory

import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self._mode = mode
        self._fd = os.open(name, mode)
        self._size = os.fstat(self._fd).st_size
        self._pos = 0
        self._buf = bytearray(8192)
        self._bufsize = 0
        self._bufpos = 0

    def close(self):
        os.close(self._fd)

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self._pos = offset
        elif whence == 1:
            self._pos += offset
        elif whence == 2:
            self._pos = self._size + offset
        else:
            raise ValueError("Invalid value for `whence`")
        return self._pos

    def tell(self):
        return self._pos

    def readable(self):
        return 'r' in self._mode

    def read(self, n):
        if not self.readable():
            raise io.Un

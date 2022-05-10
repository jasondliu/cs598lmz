import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self._fd = fd
        self._pos = 0
        self._size = os.fstat(fd).st_size

    def read(self, n=-1):
        if n == -1:
            n = self._size - self._pos
        if n <= 0:
            return b''
        data = os.read(self._fd, n)
        self._pos += len(data)
        return data

    def tell(self):
        return self._pos

    def seek(self, offset, whence=0):
        if whence == 0:
            self._pos = offset
        elif whence == 1:
            self._pos += offset
        elif whence == 2:
            self._pos = self._size + offset
        else:
            raise ValueError('invalid whence')
        if self._pos < 0:
            raise ValueError('negative seek')
        return self._pos

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):

import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r', closefd=True):
        self._file = file
        self._mode = mode
        self._closefd = closefd
        self._pos = 0
        self._size = os.fstat(file.fileno()).st_size
    def read(self, n=-1):
        if n == -1:
            n = self._size - self._pos
        if n == 0:
            return b''
        if self._pos + n > self._size:
            n = self._size - self._pos
        data = self._file.read(n)
        self._pos += len(data)
        return data
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self._pos = offset
        elif whence == io.SEEK_CUR:
            self._pos += offset
        elif whence == io.SEEK_END:
            self._pos = self._size + offset
        else:
            raise ValueError('Invalid whence

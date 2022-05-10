import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._path = path
        self._file = io.open(self._path, 'rb')
        self._size = os.path.getsize(self._path)
        self._pos = 0
    def read(self, size = -1):
        if size < 0:
            size = self._size - self._pos
        if size == 0:
            return b''
        self._pos += size
        return self._file.read(size)
    def seek(self, pos, whence = io.SEEK_SET):
        if whence == io.SEEK_SET:
            self._pos = pos
        elif whence == io.SEEK_CUR:
            self._pos += pos
        elif whence == io.SEEK_END:
            self._pos = self._size + pos
        self._file.seek(self._pos, io.SEEK_SET)
    def tell(self):
        return self._pos
    def __repr__(self):
        return f'File({self._path})'


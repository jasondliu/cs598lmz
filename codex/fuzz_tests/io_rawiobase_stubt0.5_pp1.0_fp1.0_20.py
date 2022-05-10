import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self._path = path
        self._mode = mode
        self._file = None
        self._pos = 0
        self._size = 0
        self._open()
    def _open(self):
        if self._file is None:
            self._file = open(self._path, self._mode)
            self._size = os.path.getsize(self._path)
    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None
    def fileno(self):
        self._open()
        return self._file.fileno()
    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            self._pos = offset
        elif whence == os.SEEK_CUR:
            self._pos += offset
        elif whence == os.SEEK_END:
            self._pos = self._size + offset
        else:
            raise ValueError('Invalid whence argument')

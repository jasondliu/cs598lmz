import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._path = path
        self._fd = None
    def close(self):
        if self._fd is not None:
            _os.close(self._fd)
            self._fd = None
        return super(File, self).close()
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def _open(self, mode):
        if self._fd is not None:
            raise UnsupportedOperation('File already opened')
        self._fd = _os.open(self._path, mode)
    def _seek(self, offset, whence=_os.SEEK_SET):
        if self._fd is None:
            self._open(0)
        return _os.lseek(self._fd, offset, whence)
    def tell(self):
        return self._seek(0, _os.SEEK_CUR)
    def readinto(self, buf):
        if self._fd is None:
            self._

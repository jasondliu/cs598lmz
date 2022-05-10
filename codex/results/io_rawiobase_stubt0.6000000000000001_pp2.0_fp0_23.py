import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self._path = path
        self._mode = mode
        self._file = None
        self._open()
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.close()
    def _open(self):
        self._file = open(self._path, self._mode)
    def close(self):
        if self._file:
            self._file.close()
            self._file = None
    def fileno(self):
        return self._file.fileno()
    def isatty(self):
        return self._file.isatty()
    def readable(self):
        return self._file.readable()
    def readline(self, size=-1):
        return self._file.readline(size)
    def readlines(self, hint=-1):
        return self._file.readlines(hint)
    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.

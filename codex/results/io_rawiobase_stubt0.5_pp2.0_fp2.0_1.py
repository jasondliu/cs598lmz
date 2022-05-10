import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self._filename = filename
        self._mode = mode
        self._file = None
    def close(self):
        if self._file:
            self._file.close()
        return True
    def fileno(self):
        return self._file.fileno()
    def flush(self):
        return self._file.flush()
    def isatty(self):
        return self._file.isatty()
    def readable(self):
        return self._file.readable()
    def readline(self, size=-1):
        return self._file.readline(size)
    def readlines(self, hint=-1):
        return self._file.readlines(hint)
    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)
    def seekable(self):
        return self._file.seekable()
    def tell(self):
        return self._file.tell()
    def writable(self):
        return self

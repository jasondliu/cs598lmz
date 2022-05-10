import io
class File(io.RawIOBase):
    def __init__(self, file, mode='r'):
        self._file = file
        self._mode = mode
    def read(self, n=-1):
        return self._file.read(n)
    def write(self, b):
        self._file.write(b)
        return len(b)
    def seek(self, offset, whence=io.SEEK_SET):
        self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def close(self):
        self._file.close()
    def fileno(self):
        return self._file.fileno()
    def flush(self):
        self._file.flush()
    def isatty(self):
        return self._file.isatty()
    def readable(self):
        return 'r' in self._mode
    def seekable(self):
        return self._file.seekable()
    def writable(self):
        return 'w' in self._mode
    def readline(self, limit=-1

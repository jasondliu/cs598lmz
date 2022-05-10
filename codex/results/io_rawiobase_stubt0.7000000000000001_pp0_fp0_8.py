import io
class File(io.RawIOBase):
    _fd = None
    def __init__(self, name, mode='r', data=None):
        self.name = name
        self.mode = mode
        self.pos = 0
        self._cached_data = data
    def close(self):
        self._fd.close()
    def fileno(self):
        return self._fd.fileno()
    def flush(self):
        pass
    def isatty(self):
        return False
    def read(self, n):
        return self._fd.read(n)
    def readable(self):
        return self._fd.readable()
    def readline(self, limit=-1):
        return self._fd.readline(limit)
    def readlines(self, hint=-1):
        return self._fd.readlines(hint)
    def seek(self, offset, whence=0):
        self._fd.seek(offset, whence)
    def seekable(self):
        return True
    def tell(self):
        return self._fd.tell()
    def truncate(

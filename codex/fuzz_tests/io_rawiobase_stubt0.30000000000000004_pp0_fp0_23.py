import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self._file = io.open(path, mode)
    def close(self):
        self._file.close()
    def fileno(self):
        return self._file.fileno()
    def isatty(self):
        return self._file.isatty()
    def read(self, size=-1):
        return self._file.read(size)
    def readable(self):
        return self._file.readable()
    def readinto(self, b):
        return self._file.readinto(b)
    def readline(self, size=-1):
        return self._file.readline(size)
    def readlines(self, hint=-1):
        return self._file.readlines(hint)
    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)
    def seekable(self):
        return self._file.seekable()
    def tell(self):
        return self._file.tell()
    def truncate(self

import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        self._file = io.open(*args, **kwargs)
        self._file.__class__ = io.IOBase
    def __getattr__(self, name):
        return getattr(self._file, name)
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def fileno(self):
        return None
    def close(self):
        self._file.close()
    def flush(self):
        self._file.flush()
    def read(self, size=-1):
        return self._file.read(size)
    def readall(self):
        return self._file.readall()
    def readinto(self, b):
        return self._file.readinto(b)
    def readline(self, size=-1):
        return self._file.readline(size)
    def readlines(self, hint=-1):
        return self._file.readlines(h

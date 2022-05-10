import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r', *args, **kwargs):
        super().__init__()
        self._filename = filename
        self._mode = mode
        self._args = args
        self._kwargs = kwargs
        self._file = None
        self._pos = 0
    def close(self):
        if self._file:
            self._file.close()
            self._file = None
    def readable(self):
        return 'r' in self._mode
    def writable(self):
        return 'w' in self._mode
    def seekable(self):
        return True
    def readinto(self, b):
        self._ensure_open()
        n = self._file.readinto(b)
        self._pos += n
        return n
    def read(self, n=-1):
        self._ensure_open()
        if n < 0:
            retval = self._file.read()
            self._pos = self.tell()
        else:
            retval = self._file.read

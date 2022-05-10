import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self._file = None
        self._open()
    def _open(self):
        self._file = open(self.name, self.mode)
    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None
    def readable(self):
        return self._file.readable()
    def writable(self):
        return self._file.writable()
    def seekable(self):
        return self._file.seekable()
    def seek(self, offset, whence=0):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def read(self, size=-1):
        return self._file.read(size)
    def readall(self):
        return self._file.readall()
    def readinto(self, b):
        return self._file.readinto(b)


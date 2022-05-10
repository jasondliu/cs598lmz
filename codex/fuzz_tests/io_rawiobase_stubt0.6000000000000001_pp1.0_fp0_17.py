import io
class File(io.RawIOBase):
    def __init__(self, name, mode, buffering=-1):
        super().__init__()
        self._name = name
        self._mode = mode
        self._file = open(name, mode, buffering)
    def close(self):
        self._file.close()
    def read(self, size=-1):
        return self._file.read(size)
    def readinto(self, buf):
        return self._file.readinto(buf)
    def readall(self):
        return self._file.readall()
    def write(self, buf):
        return self._file.write(buf)
    def tell(self):
        return self._file.tell()
    def seek(self, offset, whence=io.SEEK_SET):
        self._file.seek(offset, whence)
    def truncate(self, size=None):
        self._file.truncate(size)
    def flush(self):
        self._file.flush()
    def readable(self):
        return True
    def writable(self):

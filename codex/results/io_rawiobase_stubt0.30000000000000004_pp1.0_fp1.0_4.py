import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self._filename = filename
        self._mode = mode
        self._file = None
        self._open()
    def _open(self):
        self._file = open(self._filename, self._mode)
    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None
    def __del__(self):
        self.close()
    def readable(self):
        return 'r' in self._mode
    def writable(self):
        return 'w' in self._mode
    def seekable(self):
        return True
    def readinto(self, b):
        return self._file.readinto(b)
    def write(self, b):
        return self._file.write(b)
    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def fileno(

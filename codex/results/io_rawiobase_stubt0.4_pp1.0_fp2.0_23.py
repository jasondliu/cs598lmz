import io
class File(io.RawIOBase):
    def __init__(self, filename, mode='r'):
        self._filename = filename
        self._mode = mode
        self._handle = None
    def __del__(self):
        self.close()
    def close(self):
        if self._handle is not None:
            self._handle.close()
            self._handle = None
    def readable(self):
        return 'r' in self._mode
    def writable(self):
        return 'w' in self._mode
    def seekable(self):
        return True
    def readinto(self, b):
        return self._handle.readinto(b)
    def write(self, b):
        return self._handle.write(b)
    def seek(self, offset, whence=io.SEEK_SET):
        return self._handle.seek(offset, whence)
    def tell(self):
        return self._handle.tell()
    def fileno(self):
        return self._handle.fileno()
    def flush(self):
        return self._handle.flush()
   

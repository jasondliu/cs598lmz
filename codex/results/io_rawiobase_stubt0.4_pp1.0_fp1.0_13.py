import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self._name = name
        self._mode = mode
        self._file = None
        self._open()
    def _open(self):
        self._file = open(self._name, self._mode)
    def close(self):
        self._file.close()
    def readable(self):
        return self._file.readable()
    def readinto(self, b):
        return self._file.readinto(b)
    def writeable(self):
        return self._file.writeable()
    def write(self, b):
        return self._file.write(b)
    def seekable(self):
        return self._file.seekable()
    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def fileno(self):
        return self._file.fileno()
    def flush(self):
        return self._file.flush()
   

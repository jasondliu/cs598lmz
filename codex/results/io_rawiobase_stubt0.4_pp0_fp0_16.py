import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self._file = file
        super(File, self).__init__(*args, **kwargs)
    def close(self):
        self._file.close()
    def readinto(self, b):
        return self._file.readinto(b)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        return self._file.seek(offset, whence)
    def tell(self):
        return self._file.tell()
    def read(self, n=-1):
        return self._file.read(n)
    def readall(self):
        return self._file.readall()
    def readline(self, limit=-1):
        return self._file.readline(limit)
    def readlines(self, hint=-1):
        return self._file.readlines(hint)
    def truncate

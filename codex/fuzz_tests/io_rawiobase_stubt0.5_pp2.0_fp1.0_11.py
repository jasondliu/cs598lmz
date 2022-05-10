import io
class File(io.RawIOBase):
    def __init__(self, fp):
        self._fp = fp
        self.mode = fp.mode
        self.name = fp.name
        self.closed = False
    def close(self):
        self._fp.close()
        self.closed = True
    def fileno(self):
        return self._fp.fileno()
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self, offset, whence=0):
        return self._fp.seek(offset, whence)
    def tell(self):
        return self._fp.tell()
    def read(self, n):
        return self._fp.read(n)
    def write(self, b):
        return self._fp.write(b)
    def readinto(self, b):
        return self._fp.readinto(b)
    def readall(self):
        return self._fp.readall()
    def readline(self, limit=-1):

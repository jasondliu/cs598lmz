import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def fileno(self):
        return self.file.fileno()
    def readinto(self, b):
        return self.file.readinto(b)
    def readall(self):
        return self.file.readall()
    def read(self, n=-1):
        return self.file.read(n)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def truncate(self, size=None):
        return self.file.truncate(size)
    def write(self, b):
        raise io.UnsupportedOperation
    def flush(self):
        return self.file.flush()
    def close(self):
        return self.file.close()
    def __del__(

import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def open(self):
        self.file = open(self.filename, 'rb')
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def readinto(self, b):
        return self.file.readinto(b)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def truncate(self, size=None):
        raise io.UnsupportedOperation
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        pass
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b

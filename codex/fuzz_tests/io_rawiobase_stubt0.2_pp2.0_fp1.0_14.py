import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, buf):
        return self.file.readinto(buf)
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
    def read(self, n=-1):
        return self.file.read(n)
    def write(self, b):
        raise io.UnsupportedOperation("File objects are read-only")
    def fileno(self):
        return self.file.fileno()
    def flush(self):
        return self.file.flush()

import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'rb')
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def readable(self):
        return True
    def readinto(self, b):
        return self.file.readinto(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()
    def writable(self):
        return False
    def write(self, b):
        raise io.UnsupportedOperation
    def read(self, n=-1):
        return self.file.read(n)
    def readall(self):
        return self.file.readall()
    def readline(self, limit=-1):
        return self

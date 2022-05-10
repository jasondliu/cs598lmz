import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.handle = None
    def open(self):
        self.handle = open(self.name, 'rb')
        return self
    def close(self):
        if self.handle:
            self.handle.close()
            self.handle = None
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def readinto(self, b):
        return self.handle.readinto(b)
    def readall(self):
        return self.handle.readall()
    def read(self, n=-1):
        return self.handle.read(n)
    def seek(self, offset, whence=0):
        return self.handle.seek(offset, whence)
    def tell(self):
        return self.handle.tell()
    def truncate(self, size=None):
        return self.handle.truncate(size)
    def __enter__(self):
        return

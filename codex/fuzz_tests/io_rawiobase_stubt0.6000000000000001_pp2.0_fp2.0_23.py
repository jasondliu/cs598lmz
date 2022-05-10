import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
    def readinto(self, b):
        with open(self.path, 'rb') as f:
            n = f.readinto(b)
            return n
    def close(self):
        pass
    def flush(self):
        pass
    def readable(self):
        return True
    def read(self, n=-1):
        with open(self.path, 'rb') as f:
            data = f.read(n)
            return data
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        with open(self.path, 'rb') as f:
            f.seek(offset, whence)
    def tell(self):
        with open(self.path, 'rb') as f:
            return f.tell()
    def truncate(self, size=None):
        with open(self.path, 'rb') as f:
            f.truncate(size)
    def writable(self):
        return

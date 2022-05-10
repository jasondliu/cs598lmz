import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def fileno(self):
        return self.f.fileno()
    def seekable(self):
        return self.f.seekable()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        b[:n] = data
        return n
    def truncate(self, size=None):
        self.f.truncate(size)
    def flush(self):
        self.f.flush()
    def close(self):
        self.f.close()

def open(file, mode="r", buffering

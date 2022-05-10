import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def readinto(self, b):
        return self.f.readinto(b)
    def write(self, b):
        return self.f.write(b)
    def seek(self, n, whence=0):
        return self.f.seek(n, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()

def open(name, mode="r", buffering=None):
    return File(io.open(name, mode, buffering))

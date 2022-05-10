import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def readinto(self, b):
        return self.f.readinto(b)
    def seek(self, n):
        return self.f.seek(n)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()
    def fileno(self):
        return self.f.fileno()
    def flush(self):
        return self.f.flush()
    def mode(self):
        return self.f.mode()
    def name(self):
        return self.f.name()

class BufferedFile(io.BufferedIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def readinto(self, b):
        return self.f.readinto(b)
    def seek

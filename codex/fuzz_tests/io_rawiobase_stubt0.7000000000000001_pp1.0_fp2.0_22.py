import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.f = open(name, "rb")
    def close(self):
        return self.f.close()
    def seek(self, pos, whence=0):
        return self.f.seek(pos, whence)
    def tell(self):
        return self.f.tell()
    def write(self, b):
        return self.f.write(b)
    def flush(self):
        return self.f.flush()
    def readinto(self, b):
        return self.f.readinto(b)
    def readall(self):
        return self.f.readall()
    def read(self, n=-1):
        return self.f.read(n)
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def __repr__(self):
        return "<%s name=%r>" % (self.__class__.__name__, self

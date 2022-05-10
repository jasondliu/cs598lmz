import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def readall(self):
        return self.f.readall()
    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        b[:n] = data
        return n
    def write(self, b):
        self.f.write(b)
        return len(b)
    def seek(self, n, whence=0):
        return self.f.seek(n, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()
    def flush(self):
        return self.f.flush()
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    def readable(self):
        return True
    def writ

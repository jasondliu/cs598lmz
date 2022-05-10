import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.fd = f.fileno()
        self.mode = f.mode
        self.name = f.name
        self.isatty = f.isatty
    def close(self):
        self.f.close()
    def fileno(self):
        return self.fd
    def flush(self):
        self.f.flush()
    def readinto(self, b):
        return self.f.readinto(b)
    def read(self, n=-1):
        return self.f.read(n)
    def readall(self):
        return self.f.readall()
    def readline(self, limit=-1):
        return self.f.readline(limit)
    def seek(self, offset, whence=io.SEEK_SET):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def write(self, b):
        return self.f.write(b

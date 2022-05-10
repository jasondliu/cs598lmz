import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def close(self):
        self.f.close()
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    def read(self, n=-1):
        return self.f.read(n)
    def readable(self):
        return True
    def readinto(self, b):
        return self.f.readinto(b)
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def seekable(self):
        return True
    def tell(self):
        return self.f.tell()
    def truncate(self, size=None):
        return self.f.truncate(size)
    def writable(self):
        return True
    def write(self, b):
        return self.f.write(b)
    def writelines(self, lines):
        return self.f.writelines

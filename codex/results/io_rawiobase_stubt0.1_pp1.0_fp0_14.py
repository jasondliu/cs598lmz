import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def close(self):
        return self.f.close()
    def flush(self):
        return self.f.flush()
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    def readable(self):
        return self.f.readable()
    def seekable(self):
        return self.f.seekable()
    def writable(self):
        return self.f.writable()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def readinto(self, b):
        return self.f.readinto(b)
    def truncate(self, size=

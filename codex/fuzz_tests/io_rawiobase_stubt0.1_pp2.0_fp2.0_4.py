import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
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
        return self.f.readable()
    def writable(self):
        return self.f.writable()
    def seekable(self):
        return self.f.seekable()
    def __repr__(self):
        return repr(self.f)
    def __str__(self):
        return str(self

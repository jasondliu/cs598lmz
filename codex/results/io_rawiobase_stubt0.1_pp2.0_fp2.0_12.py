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
    def fileno(self):
        return self.f.fileno()
    def flush(self):
        return self.f.flush()
    def isatty(self):
        return self.f.isatty()
    def readable(self):
        return self.f.readable()
    def readline(self, limit=-1):
        return self.f.readline(limit)
    def readlines(self, hint=-1):
        return self.f.readlines(hint)
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def seekable(self):
        return self.f.seekable()
    def tell(self):
        return self.f.tell()


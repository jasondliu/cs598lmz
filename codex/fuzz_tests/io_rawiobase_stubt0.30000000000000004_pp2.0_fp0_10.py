import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()
    def flush(self):
        return self.f.flush()
    def fileno(self):
        return self.f.fileno()
    def readable(self):
        return True
    def writable(self):
        return True
    def isatty(self):
        return self.f.isatty()
    def __next__(self):
        return next(self.f)
    def __iter__(self):
        return self.f
    def __enter__(self):
        return self
    def

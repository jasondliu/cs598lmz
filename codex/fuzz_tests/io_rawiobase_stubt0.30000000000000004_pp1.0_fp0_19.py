import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def fileno(self):
        return self.f.fileno()
    def close(self):
        return self.f.close()
    @property
    def name(self):
        return self.f.name
    @property
    def mode(self):
        return self.f.mode
    @property
    def closed(self):
        return self.f.closed
    def flush(self):
        self.f.flush()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def __repr__

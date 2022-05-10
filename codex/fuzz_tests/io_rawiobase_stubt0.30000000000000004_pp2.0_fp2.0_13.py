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
    def seekable(self):
        return self.f.seekable()
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()
    def readable(self):
        return self.f.readable()
    def writable(self):
        return self.f.writable()
    def flush(self):
        return self.f.flush()
    def truncate(self, size=None):
        return self.f.truncate(size)
    def __repr__(self):
        return repr(self.f)
   

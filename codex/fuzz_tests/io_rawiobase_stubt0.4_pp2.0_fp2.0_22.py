import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def seek(self, n, whence=0):
        self.f.seek(n, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        self.f.close()
    def flush(self):
        self.f.flush()
    def fileno(self):
        return self.f.fileno()
    def isatty(self):
        return self.f.isatty()
    @property
    def closed(self):
        return self.f.closed

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if isinstance(file, str):
        return io.open(file, mode, buffering,

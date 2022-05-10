import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
    def fileno(self):
        return self.f.fileno()
    def close(self):
        self.f.close()
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
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if

import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
    def seek(self, n, whence=io.SEEK_SET):
        return self.f.seek(n, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

def file(f):
    return File(f)

def open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if not closefd:
        raise NotImplementedError("closefd=False not supported")
    if opener is not None:
        raise NotImplementedError("opener not supported")
    if newline is

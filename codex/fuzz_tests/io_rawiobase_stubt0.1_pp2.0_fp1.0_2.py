import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        self.f.close()

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    if isinstance(file, str):
        return io.open(file, mode, buffering, encoding, errors, newline, closefd, opener)
    else:
        return io.TextIOWrapper(File(file), encoding, errors, newline)

def StringIO(string=''):
    return io.StringIO(string)



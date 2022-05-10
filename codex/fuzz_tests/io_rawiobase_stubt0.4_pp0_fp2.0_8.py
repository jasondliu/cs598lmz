import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def seek(self, offset, whence=0):
        self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        self.f.close()

def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
    if newline is not None:
        raise ValueError("newline is not supported in pyopencl")
    if isinstance(file, str):
        if 'b' in mode:
            flags = os.O_RDONLY if 'r' in mode else (os.O_WRONLY | os.O_CREAT)
            fd = os.open(file, flags, 0o666)
        else:


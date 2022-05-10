import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def seekable(self):
        return True
    def readable(self):
        return True
    def seek(self, n, whence=0):
        return self.f.seek(n, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        pass

def open(f):
    return File(f)

def make_file(f):
    if isinstance(f, str):
        return open(f, "rb")
    return f

def open_or_fd(file, mode='rb'):
    if isinstance(file, int):
        return os.fdopen(file, mode, closefd=False)
    elif isinstance(file, str):
        return open(file, mode)
    elif isinstance(file, io.IOBase):
        return file
    else:
        raise TypeError("invalid file

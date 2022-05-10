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
        return True
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()

def open(file, mode='rb', buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
    if buffering == 0:
        raise ValueError("unbuffered streams must set the buffer size to 1")
    if buffering < 0:
        buffering = io.DEFAULT_BUFFER_SIZE
    if buffering < 1:
        raise ValueError("invalid buffer size")


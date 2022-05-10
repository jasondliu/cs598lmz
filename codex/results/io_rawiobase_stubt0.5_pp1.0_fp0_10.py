import io
class File(io.RawIOBase):
    def __init__(self, f, mode='rb'):
        self.f = f
        self.mode = mode
    def readable(self):
        return 'r' in self.mode
    def writable(self):
        return 'w' in self.mode
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def readinto(self, b):
        n = len(b)
        data = self.f.read(n)
        n = len(data)
        b[:n] = data
        return n
    def write(self, b):
        return self.f.write(b)
    def flush(self):
        return self.f.flush()
    def close(self):
        return self.f.close()

def open(file, mode='rb', buffering=-1, encoding=None, errors=None, newline=None, closefd=True,

import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.f = io.open(filename, mode)
    def close(self):
        if self.f:
            self.f.close()
            self.f = None
    def __del__(self):
        self.close()
    def readable(self):
        return self.mode in ('r', 'r+', 'a+')
    def writable(self):
        return self.mode in ('w', 'w+', 'a', 'a+')
    def seekable(self):
        return True
    def readinto(self, b):
        return self.f.readinto(b)
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        return self.f.write(b)
    def flush(self):
        return self.f.flush()
    def tell(self):
        return self.f.tell()
    def seek(self, offset,

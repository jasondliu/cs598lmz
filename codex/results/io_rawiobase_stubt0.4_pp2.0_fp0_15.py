import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, 'rb')
        self.size = os.fstat(self.f.fileno()).st_size
        self.pos = 0
    def read(self, n=-1):
        if n == -1:
            n = self.size - self.pos
        data = self.f.read(n)
        self.pos += len(data)
        return data
    def tell(self):
        return self.pos
    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = self.size + offset
        else:
            raise ValueError('whence must be 0, 1 or 2')
        self.f.seek(self.pos)
    def close(self):
        self.f.close()
    def __enter__(self):
        return self
    def __exit__

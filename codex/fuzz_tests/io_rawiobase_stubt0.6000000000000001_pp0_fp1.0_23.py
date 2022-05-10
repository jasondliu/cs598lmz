import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.f = io.open(name, 'rb')
        self.pos = 0
        self.size = os.path.getsize(name)
    def read(self, size=-1):
        if size < 0:
            pos = self.pos
            self.pos = self.size
            return self.f.read()[pos:]
        elif size == 0:
            return b''
        else:
            pos = self.pos
            self.pos = min(self.pos + size, self.size)
            return self.f.read(size)[pos:]
    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = self.size + offset
        else:
            raise ValueError('Invalid whence')
        return self.pos
    def tell(self):
        return self.pos
    def close(self):

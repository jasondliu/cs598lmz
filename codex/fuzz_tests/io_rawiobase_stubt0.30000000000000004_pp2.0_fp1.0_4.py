import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.pos = 0
        self.file = open(name, mode)
        self.size = os.path.getsize(name)
    def read(self, size=-1):
        if size == -1:
            size = self.size
        if self.pos + size > self.size:
            size = self.size - self.pos
        if size == 0:
            return b''
        self.file.seek(self.pos)
        data = self.file.read(size)
        self.pos += size
        return data
    def tell(self):
        return self.pos
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = self.size + pos
        else:
            raise ValueError("Invalid value for whence: %r" % (whence,))

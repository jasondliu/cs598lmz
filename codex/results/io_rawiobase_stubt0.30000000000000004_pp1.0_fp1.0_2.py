import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = open(path, 'rb')
        self.size = os.path.getsize(path)
        self.pos = 0
        self.closed = False

    def read(self, size=-1):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if size < 0:
            size = self.size - self.pos
        if self.pos + size > self.size:
            size = self.size - self.pos
        self.pos += size
        return self.file.read(size)

    def tell(self):
        return self.pos

    def seek(self, offset, whence=0):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = self.size + offset
        self.file.seek(self

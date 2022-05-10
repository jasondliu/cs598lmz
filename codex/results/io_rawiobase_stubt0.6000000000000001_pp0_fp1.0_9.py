import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None
        self.pos = 0
        self.buf = b""
    def tell(self):
        return self.pos + len(self.buf)
    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = os.path.getsize(self.name) + offset
        else:
            raise ValueError("Invalid whence value")
        if self.pos < 0:
            self.pos = 0
    def readinto(self, b):
        if self.file is None:
            self.file = open(self.name, self.mode)
        if len(b) > len(self.buf):
            self.buf += self.file.read(len(b))
        b[:len(self.buf)] = self.buf
        self.buf = b""

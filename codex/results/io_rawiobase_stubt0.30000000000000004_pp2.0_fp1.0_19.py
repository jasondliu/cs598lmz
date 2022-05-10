import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = os.open(name, os.O_RDONLY)
        self.size = os.fstat(self.fd).st_size
        self.pos = 0
    def read(self, size=-1):
        if size == -1:
            size = self.size - self.pos
        if size == 0:
            return b""
        buf = os.read(self.fd, size)
        self.pos += len(buf)
        return buf
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = self.size + pos
        else:
            raise ValueError("whence must be 0, 1 or 2")
        return self.pos
    def tell(self):
        return self.pos
    def close(self):
        os.close(self.fd)
        self.fd =

import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', closefd=True):
        self.closefd = closefd
        self.mode = mode
        self.path = path
        self.fd = os.open(path, os.O_RDONLY)
        self.pos = 0
        self.size = os.fstat(self.fd).st_size
        self.buf = bytearray(4096)

    def readinto(self, b):
        if not isinstance(b, bytearray):
            raise TypeError("argument must be a bytearray")
        if self.pos >= self.size:
            return 0
        size = len(b)
        if self.pos + size > self.size:
            size = self.size - self.pos
        os.lseek(self.fd, self.pos, 0)
        n = os.read(self.fd, self.buf, size)
        b[:n] = self.buf[:n]
        self.pos += n
        return n

    def close(self):

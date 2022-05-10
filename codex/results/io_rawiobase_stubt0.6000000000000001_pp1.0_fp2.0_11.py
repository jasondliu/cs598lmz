import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.file = open(filename, "rb")
        self.buffer = b""
        self.offset = 0
        self.size = os.fstat(self.file.fileno()).st_size
    def read(self, n=-1):
        if n == -1:
            n = self.size - self.offset
        if n == 0:
            return b''
        while len(self.buffer) < n:
            chunk = self.file.read(n - len(self.buffer))
            if len(chunk) == 0:
                break
            self.buffer += chunk
        ret, self.buffer = self.buffer[:n], self.buffer[n:]
        self.offset += len(ret)
        return ret
    def seek(self, offset, whence=0):
        if whence == 1:
            offset += self.offset
        elif whence == 2:
            offset += self.size
        assert offset >= 0
        self.buffer = b""
        self.offset = offset
        self.

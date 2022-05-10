import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self):
        self.pos = 0
        self.buf = bytearray(b'hello world')
    def readinto(self, b):
        n = len(b)
        if self.pos >= len(self.buf):
            return 0
        if n > len(self.buf) - self.pos:
            n = len(self.buf) - self.pos
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n
    def write(self, b):
        self.buf += b
        self.pos += len(b)
        return len(b)
    def tell(self):
        return self.pos
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = len(self.buf) + pos
        return

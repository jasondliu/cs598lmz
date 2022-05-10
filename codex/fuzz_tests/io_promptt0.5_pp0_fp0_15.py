import io
# Test io.RawIOBase
# io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def __init__(self, buf=None):
        self.buf = buf or b'0123456789'
        self.pos = 0
    def readinto(self, b):
        n = len(b)
        if self.pos >= len(self.buf):
            return 0
        if n > len(self.buf) - self.pos:
            n = len(self.buf) - self.pos
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n
    def seekable(self):
        return True
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        else:
            self.pos = len(self.buf) + pos
        return self.pos
    def tell(self):
        return self.pos
    def readable(self

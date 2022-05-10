import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0
    def read(self, n=-1):
        if n < 0:
            n = len(self.buf) - self.pos
        res = self.buf[self.pos:self.pos+n]
        self.pos += n
        return res
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = len(self.buf) + pos
        else:
            raise ValueError("whence must be 0, 1 or 2")
    def tell(self):
        return self.pos

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
        self.pos = 0

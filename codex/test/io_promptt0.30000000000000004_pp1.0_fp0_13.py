import io
# Test io.RawIOBase.readinto()

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0
    def readinto(self, b):
        n = min(len(b), len(self.buf) - self.pos)
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

class TestRawBufferedIO(io.BufferedIOBase):
    def __init__(self, buf):
        self.raw = TestRawIO(buf)
        self.read_buf = bytearray()
        self.read_

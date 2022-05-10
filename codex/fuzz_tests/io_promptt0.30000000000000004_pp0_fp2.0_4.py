import io
# Test io.RawIOBase.readinto()

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        if self.pos + n > len(self.buf):
            n = len(self.buf) - self.pos
            if n == 0:
                return None
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = len(self.buf) + pos
        else:
            raise ValueError("whence must be 0, 1 or 2")
        return self.pos

    def tell(self):
       

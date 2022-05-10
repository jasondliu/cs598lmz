import io
# Test io.RawIOBase.readinto()

class TestRawIO(io.RawIOBase):

    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        if self.pos >= len(self.buf):
            return 0
        if self.pos + n > len(self.buf):
            n = len(self.buf) - self.pos
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def write(self, b):
        self.buf += b
        self.pos += len(b)
        return len(b)

    def readable(self):
        return True

    def writable(self):
        return True

def test(buf, b):
    r = TestRawIO(buf)
    n = r.readinto(b)
    if n != len(buf):
        print("readinto() returned wrong value")

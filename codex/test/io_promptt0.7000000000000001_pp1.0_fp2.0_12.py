import io
# Test io.RawIOBase.readinto() in a separate test case
class MyRawIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0
    def readable(self):
        return True
    def readinto(self, buf):
        n = len(buf)
        if self.pos >= len(self.data):
            return 0
        if n > len(self.data) - self.pos:
            n = len(self.data) - self.pos
        buf[:n] = self.data[self.pos:self.pos+n]
        self.pos += n
        return n

class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
        self.pos = 0
    def readable(self):
        return True
    def readinto(self, buf):
        n = len(buf)
        if self.pos >= len(self.raw.data):
            return 0

import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, b):
        n = len(b)
        self.read(b, 0, n)
        return n
    def read(self, b, b_offset, n):
        for i in range(b_offset, b_offset+n):
            b[i] = 42
        return n

# Test io.BufferedIOBase
class BufferedI(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
        super().__init__()
    def readable(self):
        return True
    def readinto(self, b):
        return self.raw.readinto(b)
    def read(self, n=-1):
        return self.raw.read(n)

# Test io.TextIOBase
class TextI(io.TextIOBase)

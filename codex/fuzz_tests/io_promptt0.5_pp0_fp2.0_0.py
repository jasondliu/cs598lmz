import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.offset = 0
    def readable(self):
        return True
    def readinto(self, b):
        n = len(self.data) - self.offset
        if n <= 0:
            return 0
        if n > len(b):
            n = len(b)
        b[:n] = self.data[self.offset:self.offset+n]
        self.offset += n
        return n

# Test io.BufferedIOBase
class BufferedI(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
    def readable(self):
        return True
    def readinto(self, b):
        return self.raw.readinto(b)
    def read(self, n=-1):
        if n >= 0:
            b = bytearray(n)
            n = self.readinto(b)
            return bytes(b[:n

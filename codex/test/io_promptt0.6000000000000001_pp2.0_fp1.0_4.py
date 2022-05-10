import io
# Test io.RawIOBase.readinto()

class RawIOBaseSubclass(io.RawIOBase):
    def __init__(self, len):
        self.len = len
        self.pos = 0

    def readinto(self, b):
        if self.pos >= self.len:
            return None
        n = min(len(b), self.len - self.pos)
        b[:n] = list(range(self.pos, self.pos + n))
        self.pos += n
        return n

    def readable(self):
        return True


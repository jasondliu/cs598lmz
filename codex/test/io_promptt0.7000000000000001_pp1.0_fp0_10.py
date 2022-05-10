import io
# Test io.RawIOBase

bufsize = 8

class MyIO(io.RawIOBase):
    def __init__(self):
        self.pos = 0

    def seekable(self):
        return True

    def readable(self):
        return True

    def writable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = len(self.data) + pos
        return self.pos

    def tell(self):
        return self.pos

    def readinto(self, b):
        n = len(self.data) - self.pos
        if n > len(b):
            n = len(b)
        if n:
            b[:n] = self.data[self.pos:self.pos+n]
        return n

    def write(self, b):
        n = len(b)

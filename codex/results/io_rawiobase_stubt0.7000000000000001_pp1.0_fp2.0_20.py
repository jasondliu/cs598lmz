import io
class File(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def readinto(self, b):
        n = len(b)
        if self.pos + n > len(self.data):
            n = len(self.data) - self.pos
        b[:n] = self.data[self.pos:self.pos+n]
        self.pos += n
        return n
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = len(self.data) - pos
        return self.pos
    def tell(self):
        return self.pos
    def read(self, n=-1):
        if n >= 0:
            if self.pos + n > len(self.data):

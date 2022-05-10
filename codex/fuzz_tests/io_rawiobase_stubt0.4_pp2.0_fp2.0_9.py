import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.offset = 0
        self.length = 0
        self.data = b''
        self.closed = False
    def readable(self):
        return 'r' in self.mode
    def writable(self):
        return 'w' in self.mode
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.length + offset
        else:
            raise ValueError('whence must be 0, 1, or 2')
        return self.offset
    def tell(self):
        return self.offset
    def readinto(self, b):
        if self.offset < self.length:
            n = min(len(b), self.length - self.offset)
            b[:n] = self.

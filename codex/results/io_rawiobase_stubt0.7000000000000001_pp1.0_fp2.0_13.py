import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.offset = 0
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return False
    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = len(self.name) + offset
        else:
            raise ValueError("invalid whence")
        return self.offset
    def tell(self):
        return self.offset
    def readinto(self, b):
        data = self.name[self.offset:self.offset+len(b)]
        b[:len(data)] = data
        self.offset += len(data)
        return len(data)
    def read(self, n=-1):
        if n is None:
            n = -1
        data = self.name[self.offset:self.offset+n

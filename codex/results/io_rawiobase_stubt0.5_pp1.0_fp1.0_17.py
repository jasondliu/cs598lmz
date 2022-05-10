import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, size=-1):
        return open(self.name, 'rb').read(size)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return False
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def fileno(self):
        return 0
    def close(self):
        pass

class StringFile(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0
    def read(self, size=-1):
        if size < 0:
            size = len(self.data) - self.pos
        if self.pos + size > len(self.data):
            size = len(self.data) - self.pos
        self.pos += size
        return self.data[self.pos - size:self.pos]
    def readable(

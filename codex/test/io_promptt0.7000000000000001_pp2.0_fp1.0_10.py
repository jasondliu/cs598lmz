import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self):
        super().__init__()
        self.buf = b'abcdefghijklmnopqrstuvwxyz'
        self.pos = 0
    def read(self, size=-1):
        if size == -1: size = len(self.buf)
        if size == 0: return b''
        self.pos += size
        return self.buf[self.pos-size:self.pos]
    def seekable(self):
        return True
    def seek(self, pos, whence=io.SEEK_SET):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = len(self.buf) + pos
        return self.pos
    def tell(self):
        return self.pos
    def write(self, b):
        pass
# Test io.BufferedIOBase

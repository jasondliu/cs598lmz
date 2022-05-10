import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0
    def read(self, n=-1):
        if self.pos == len(self.buf):
            return b''
        if n < 0 or n > len(self.buf) - self.pos:
            n = len(self.buf) - self.pos
        ret = self.buf[self.pos:self.pos+n]
        self.pos += n
        return ret
    def write(self, b):
        self.buf += b
        return len(b)
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = len(self.buf) + pos
        else:
            raise ValueError('Invalid whence value')
        return self.pos
    def tell(self):
        return self.pos

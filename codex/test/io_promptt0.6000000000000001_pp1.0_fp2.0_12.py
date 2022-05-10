import io
# Test io.RawIOBase
class RawIOBase(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0
    def read(self, n):
        end = self.pos + n
        if end > len(self.buf):
            end = len(self.buf)
        data = self.buf[self.pos:end]
        self.pos = end
        return data
    def write(self, b):
        self.buf += b
        self.pos += len(b)
    def tell(self):
        return self.pos
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        else:
            self.pos = len(self.buf) + pos
    def close(self):
        self.buf = None
    def __del__(self):
        if self.buf is not None:
            print("unclosed file", self.buf)
# Test io.BufferedIOBase


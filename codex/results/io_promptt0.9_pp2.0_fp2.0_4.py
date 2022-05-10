import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def readline(self):
        return b"hello"
r = RawI()
r.fileno()

r.readable()
r.write(b"hello")
r.writable()
r.seekable()


class BufferedI(io.BufferedIOBase):
    def __init__(self):
        self.buf=b""
        self.pos=0

    def seekable(self):
        return True

    def readable(self):
        return True

    def seek(self,offset,whence=0):
        if whence == 0:
            self.pos=offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = len(self.buf) + offset
        return self.pos

    def tell(self):
        return self.pos

    def read(self,size):
        if self.pos >= len(self.buf):
            return b""
        else:
            chunk = self.buf[self.pos:self.

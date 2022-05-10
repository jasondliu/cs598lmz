import io
# Test io.RawIOBase.readinto()

import _io

class MyIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.offset = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = len(self.buf) + offset
        else:
            raise ValueError("whence must be 0, 1, or 2")
        return self.offset

    def tell(self):
        return self.offset

    def readinto(self, b):
        n = len(b)
        if self.offset + n > len(self.buf):
            n = len(self.buf) - self.offset
        b[:n] = self.buf[self.offset:self.offset+n]
        self.offset += n
        return n

   

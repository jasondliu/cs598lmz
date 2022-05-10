import io
# Test io.RawIOBase by wrapping it in a class that implements readinto()
class Wrapper(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.offset = 0

    def readinto(self, n):
        n = min(n, len(self.buf) - self.offset)
        self.buf[0:n] = self.buf[self.offset:self.offset + n]
        self.offset += n
        return n

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = len(self.buf) + offset
        else:
            raise ValueError("invalid whence (%r, should be 0, 1 or 2)" %
                             (whence,))
        return self.offset

buf = bytearray(b"abcdefghijklmnop")
r = Wrapper(buf)
rbuf = bytearray(5)
n

import io
# Test io.RawIOBase

# Issue #10338: check that io.RawIOBase's readinto() method works correctly
# when the underlying raw stream is in non-blocking mode.
# The test currently only checks readinto() with a bytearray argument.

class NonBlockingRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.offset = 0

    def readable(self):
        return True

    def readinto(self, b):
        if self.offset >= len(self.buf):
            return None
        n = min(len(b), len(self.buf) - self.offset)
        b[:n] = self.buf[self.offset:self.offset+n]
        self.offset += n
        return n

    def read(self, n=-1):
        if self.offset >= len(self.buf):
            return None
        if n < 0:
            n = len(self.buf) - self.offset
        res = self.buf[self.offset:self.offset+n]
       

import io
# Test io.RawIOBase.readinto()

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.offset = 0
    def readinto(self, b):
        n = len(b)
        if self.offset + n > len(self.buf):
            n = len(self.buf) - self.offset
            b = memoryview(b)[:n]
        b[:] = self.buf[self.offset:self.offset+n]
        self.offset += n
        return n
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return False

buf = b'abcdefghijklmnopqrstuvwxyz'

# Try with a bytearray
b = bytearray(26)
f = TestRawIO(buf)
n = f.readinto(b)
assert n == len(buf)
assert b == buf

# Try with a memoryview
b = memoryview(by

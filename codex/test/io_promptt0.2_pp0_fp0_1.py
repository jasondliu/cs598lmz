import io
# Test io.RawIOBase.readinto()

# Check that readinto() works with a memoryview

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def readinto(self, b):
        n = min(len(self.buf)-self.pos, len(b))
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n

    def readable(self):
        return True

buf = b"hello world"
r = TestRawIO(buf)
b = bytearray(5)
n = r.readinto(b)
print(n, b)
n = r.readinto(b)
print(n, b)

m = memoryview(b)
n = r.readinto(m)
print(n, m)
n = r.readinto(m)
print(n, m)

# Check that readinto() works with a bytearray


import io
# Test io.RawIOBase.readinto()

# Test readinto() with a bytearray

class TestRawIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def readinto(self, b):
        n = len(self.data) - self.pos
        if n > len(b):
            n = len(b)
        if n > 0:
            b[:n] = self.data[self.pos:self.pos+n]
        self.pos += n
        return n

    def readable(self):
        return True

data = b'abcdefghijklmnopqrstuvwxyz'

for n in range(len(data) + 1):
    b = bytearray(n)
    f = TestRawIO(data)
    m = f.readinto(b)
    if m != n:
        print('readinto() returned %d, expected %d' % (m, n))
    if b != data[:n]:
        print

import io
# Test io.RawIOBase.readinto()

import _io

class MyRawIO(_io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0
    def readinto(self, b):
        n = len(b)
        if self.pos + n > len(self.buf):
            n = len(self.buf) - self.pos
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n
    def readable(self):
        return True

buf = bytearray(b'abcdefghijklmnopqrstuvwxyz')

# Test readinto() with a bytearray
r = MyRawIO(buf)
b = bytearray(10)
n = r.readinto(b)
assert n == 10
assert b == buf[:10]
assert r.pos == 10

# Test readinto() with a memoryview
r = MyRawIO(buf)
b = memoryview(byt

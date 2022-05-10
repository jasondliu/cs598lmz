import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def __init__(self):
        self.pos = 0
        self.buffer = b''

    def readinto(self, b):
        n = len(b)
        if self.pos + n > len(self.buffer):
            n = len(self.buffer) - self.pos
        b[:n] = self.buffer[self.pos:self.pos + n]
        self.pos += n
        return n

    def write(self, b):
        self.buffer += b


r = MyRawIO()
r.write(b'abcdefghi')
b = bytearray(5)
n = r.readinto(b)
print(b[:n])
n = r.readinto(b)
print(b[:n])
n = r.readinto(b)
print(n)
print(b[:n])

# test a readinto() that is interrupted by a signal
import signal
import os


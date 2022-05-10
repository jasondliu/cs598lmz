import io
# Test io.RawIOBase.readinto()

import _io

class MyRawIO(_io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf

    def readinto(self, b):
        n = len(b)
        n = min(n, len(self.buf))
        b[:n] = self.buf[:n]
        self.buf = self.buf[n:]
        return n

    def write(self, b):
        self.buf += b

def test(buf):
    print(buf)
    f = MyRawIO(buf)
    b = bytearray(len(buf))
    n = f.readinto(b)
    print(n, repr(b[:n]), repr(b[n:]))
    if n != len(buf):
        raise ValueError("readinto() returned wrong number of bytes")
    if b[:n] != buf:
        raise ValueError("readinto() returned wrong bytes")

test(b"hello")
test(b"hello world")
test(b"

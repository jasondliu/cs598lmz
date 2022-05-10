import io
# Test io.RawIOBase.readinto()

import _io

class MyRawIO(_io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0
    def readinto(self, b):
        n = min(len(b), len(self.buf) - self.pos)
        b[:n] = self.buf[self.pos:self.pos+n]
        self.pos += n
        return n
    def readable(self):
        return True

def test_readinto():
    b = bytearray(b"abc")
    r = MyRawIO(b)
    a = bytearray(10)
    n = r.readinto(a)
    assert n == 3
    assert a[:3] == b
    assert a[3:] == b"\0\0\0\0\0"
    n = r.readinto(a)
    assert n == 0
    assert a[:3] == b
    assert a[3:] == b"\0\0\0

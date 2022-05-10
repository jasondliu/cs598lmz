import io
# Test io.RawIOBase.readinto()

import _io

class BytesIO(io.RawIOBase):
    def __init__(self, s):
        self.buf = s
    def readable(self):
        return True
    def readinto(self, buf):
        n = len(buf)
        if n > len(self.buf):
            n = len(self.buf)
        buf[:n] = self.buf[:n]
        self.buf = self.buf[n:]
        return n

def test(s):
    b = BytesIO(s)
    buf = bytearray(len(s) * 2)
    n = b.readinto(buf)
    assert n == len(s)
    assert buf[:n] == s
    assert buf[n:] == b"\x00\x00\x00" * n
    assert b.readinto(buf) == 0


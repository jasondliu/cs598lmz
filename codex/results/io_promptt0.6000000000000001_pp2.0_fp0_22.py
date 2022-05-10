import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def __init__(self):
        self.pos = 0

    def read(self, n=-1):
        if n < 0:
            return b"abcde"
        else:
            return b"abcde"[:n]

    def readinto(self, b):
        n = len(b)
        b[:5] = b"abcde"
        return n

    def write(self, b):
        return len(b)

    def seek(self, pos, whence=0):
        self.pos = pos
        return pos

    def tell(self):
        return self.pos

    def close(self):
        pass

rawio = MyRawIO()

# Test read
with rawio as f:
    assert f.read(1) == b'a'
    assert f.read(2) == b'bc'
    assert f.read() == b'de'
    assert f.read() == b''
    assert f.read(1) == b

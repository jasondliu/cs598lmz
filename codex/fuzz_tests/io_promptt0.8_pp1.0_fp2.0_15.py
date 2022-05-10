import io
# Test io.RawIOBase.read1()
import io

class BlobIO(io.RawIOBase):
    def __init__(self, b):
        self.b = b

    def readinto(self, buf):
        if len(buf) > len(self.b):
            buf[:len(self.b)] = self.b
            self.b = b''
            return len(self.b)
        else:
            buf[:] = self.b[:len(buf)]
            self.b = self.b[len(buf):]
            return len(buf)

    def read1(self, n):
        if len(self.b) > n:
            r = self.b[:n]
            self.b = self.b[n:]
            return r
        else:
            r = self.b
            self.b = b''
            return r

def test_read1():
    for s in [b'', b'a', b'abc', b'a'*10000]:
        with BlobIO(s) as f:
            rest =

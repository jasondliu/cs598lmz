import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def __init__(self, buf):
        self._buf = buf
        self._pos = 0

    def readinto(self, b):
        if len(b) > len(self._buf) - self._pos:
            raise EOFError
        b[:len(self._buf) - self._pos] = self._buf[self._pos:]
        self._pos = len(self._buf)
        return len(self._buf) - self._pos

    def readable(self):
        return True

for buf in [ b'abc', bytearray(b'abc'), memoryview(b'abc') ]:
    r = MyRawIO(buf)
    b = bytearray(2)
    n = r.readinto(b)
    print(n, repr(b[:n]))
    try:
        n = r.readinto(b)
        print(n, repr(b[:n]))
    except EOFError:
        print('EOF')

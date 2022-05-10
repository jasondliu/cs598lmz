import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self):
        self.pos = 0
    def read(self, n):
        return 'a' * n
    def seekable(self):
        return True
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = 100 + pos
        else:
            raise ValueError("Invalid whence (%s, should be 0, 1 or 2)" % (whence,))
    def tell(self):
        return self.pos

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self._raw = raw
    def read(self, n=-1):
        return self._raw.read(n)
    def seek(self, pos, whence=0):
        return self._raw.seek(pos, whence)

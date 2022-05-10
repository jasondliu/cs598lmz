import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self):
        self.pos = 0
    def read(self, count=None):
        if count is None:
            count = self.pos
        else:
            count = min(count, self.pos)
        self.pos -= count
        return b"\x00" * count
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = 0
        return self.pos
    def tell(self):
        return self.pos
    def truncate(self, size=None):
        if size is not None:
            self.pos = min(self.pos, size)
        return self.pos

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self._raw = raw
    def read(self, count=None

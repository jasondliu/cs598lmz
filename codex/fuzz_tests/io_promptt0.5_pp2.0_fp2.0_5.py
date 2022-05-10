import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self, raw):
        self.raw = raw
    def read(self, n=-1):
        return self.raw.read(n)
    def write(self, b):
        return self.raw.write(b)
    def seek(self, n, whence=0):
        return self.raw.seek(n, whence)
    def tell(self):
        return self.raw.tell()
    def readinto(self, b):
        return self.raw.readinto(b)
    def truncate(self, size=None):
        return self.raw.truncate(size)
    def close(self):
        return self.raw.close()
    @property
    def closed(self):
        return self.raw.closed

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
    def read(self, n=-1):
        return self.raw

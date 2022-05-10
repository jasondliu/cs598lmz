import io
# Test io.RawIOBase inheritance
class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        n = len(b)
        b[:] = n * b'\x00'
        return n
r = MyRawIO()
print(r.read(4))

# Test io.BufferedIOBase inheritance
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw  # should be a RawIOBase object
    def read(self, n=-1):
        return self.raw.read(n)
    def write(self, b):
        return self.raw.write(b)
    def raw_read(self, n):
        return self.raw.read(n)
    def raw_write(self, b):
        return self.raw.write(b)
b = MyBufferedIO(r)
print(b.read(4))

# Test io.IOBase inheritance
class MyIO(io.IOBase):
    def read(self, n=-1):
        return

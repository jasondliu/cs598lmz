import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'\x00'*n
    def write(self, b):
        return len(b)

m = MyRawIO()
print(m.read(10))
print(m.write(b'abcdef'))

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
    def read(self, n=-1):
        return self.raw.read(n)
    def write(self, b):
        n = self.raw.write(b)
        return n
    def seek(self, n):
        return self.raw.seek(n)
    def tell(self):
        return self.raw.tell()

m = MyBufferedIO(MyRawIO())
print(m.read(10))
print(m.write(b'abcdef'))

# Test io.TextIOBase

import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'0' * n
    def write(self, b):
        return len(b)

r = MyRawIO()
print(r.read(10))
print(r.write(b'abcdef'))
print(r.fileno())

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
    def read(self, n=-1):
        return self.raw.read(n)
    def write(self, b):
        return self.raw.write(b)
    def flush(self):
        return

b = MyBufferedIO(r)
print(b.read(10))
print(b.write(b'abcdef'))
print(b.flush())

# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def __init__(self, raw):
        self

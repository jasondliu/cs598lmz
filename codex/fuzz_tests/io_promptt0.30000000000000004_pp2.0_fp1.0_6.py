import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b'\x00'*n
    def write(self, b):
        return len(b)

with MyRawIO() as f:
    print(f.read(10))
    print(f.write(b'abcde'))

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw
    def read(self, n=-1):
        return self.raw.read(n)
    def write(self, b):
        return self.raw.write(b)
    def flush(self):
        pass

with MyBufferedIO(MyRawIO()) as f:
    print(f.read(10))
    print(f.write(b'abcde'))

# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def __init__(self, raw):
        self.raw =

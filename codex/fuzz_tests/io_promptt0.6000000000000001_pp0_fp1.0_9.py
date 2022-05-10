import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):

    def read(self, n=-1):
        return b"x" * n

with MyRawIO() as f:
    print(f.read())

with MyRawIO() as f:
    print(f.read(5))
    print(f.read())

with MyRawIO() as f:
    print(f.read(5))
    print(f.read(5))
    print(f.read())

# Test io.BufferedIOBase
class MyBufferedIO(io.BufferedIOBase):

    def __init__(self):
        self.read_calls = 0

    def read(self, n=-1):
        self.read_calls += 1
        return b"x" * n

    def read1(self, n):
        self.read_calls += 1
        return b"x" * n

with MyBufferedIO() as f:
    print(f.read())
    print(f.read())
    print(f.read())
   

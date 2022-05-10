import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"\x00"*n
    def write(self, b):
        return len(b)

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

# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def __init__(self, raw):
        self.raw = raw
    def read(self, n=-1):
        return self.raw.read(n).decode("utf-8")
    def write(self, b):
        return self.raw.write(b.encode("utf-8"))
    def flush(self):
        return

# Test io.

import io
# Test io.RawIOBase

class SimpleRawIO(io.RawIOBase):
    def __init__(self):
        self.len = 0

    def readinto(self, b):
        n = len(b)
        self.len += n
        return n

r = SimpleRawIO()
buf = bytearray(100)
n = r.readinto(buf)
print(n)
n = r.readinto(buf)
print(n)

# Test io.BufferedIOBase

class SimpleBufferedIO(io.BufferedIOBase):
    def __init__(self):
        self.len = 0

    def readinto(self, b):
        n = len(b)
        self.len += n
        return n

r = SimpleBufferedIO()
buf = bytearray(100)
n = r.readinto(buf)
print(n)
n = r.readinto(buf)
print(n)

# Test io.TextIOBase

class SimpleTextIO(io.TextIOBase):
    def __init__(self

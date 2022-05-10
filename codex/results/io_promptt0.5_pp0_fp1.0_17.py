import io
# Test io.RawIOBase.readinto()

try:
    io.RawIOBase.readinto
except AttributeError:
    import sys
    print("SKIP")
    sys.exit()

class TestRawIOBase(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def readinto(self, buf):
        n = min(len(buf), len(self.data) - self.pos)
        buf[:n] = self.data[self.pos:self.pos + n]
        self.pos += n
        return n

    def readable(self):
        return True

buf = bytearray(5)

# readinto returns number of bytes read
r = TestRawIOBase(b"12345")
print(r.readinto(buf))
print(buf)

# readinto returns None at EOF
r = TestRawIOBase(b"12345")
r.readinto(buf)
r.readinto(buf)
print(r.readinto(buf))



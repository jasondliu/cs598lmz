import io
# Test io.RawIOBase.readinto()
try:
    io.RawIOBase.readinto
except AttributeError:
    print('SKIP')
    raise SystemExit

# https://bugs.python.org/issue37600
class MyIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def readable(self):
        return True

    def readinto(self, buf):
        if self.pos >= len(self.data):
            return None
        n = min(len(self.data) - self.pos, len(buf))
        buf[:n] = self.data[self.pos:self.pos + n]
        self.pos += n
        return n

data = b'abcdefg'
buf = bytearray(len(data))
f = MyIO(data)
print(f.readinto(buf))
print(buf)

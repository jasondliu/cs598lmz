import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'abc'
    def seekable(self):
        return True
    def writable(self):
        return True

f = File()
f.write(b'abc')
f.seek(0)
print(f.read(1))
print(f.read(1))
print(f.read(1))
print(f.read(1))

# io.BufferedReader()
class BufferedReader(io.RawIOBase):
    def __init__(self, raw):
        self.raw = raw
        self.buffer = b''
    def read(self, n=-1):
        if n == -1:
            n = len(self.buffer)
        while len(self.buffer) < n:
            self.buffer += self.raw.read(64)
        data = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return data
    def readable(self):
        return True

f2 = BufferedReader(f)
print(f2

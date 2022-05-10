import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.file = open(filename, 'rb')
        self.buffer = b""

    def read(self, sz):
        while len(self.buffer) < sz:
            self.buffer += self.file.read(sz)
        data, self.buffer = self.buffer[:sz], self.buffer[sz:]
        return data

f = File('/etc/passwd')
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(

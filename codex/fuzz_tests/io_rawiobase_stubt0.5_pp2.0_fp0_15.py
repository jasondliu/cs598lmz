import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.f = open(name, 'rb')
        self.n = 0
    def read(self, size=-1):
        self.n += 1
        if self.n % 100 == 0:
            print('read', self.n)
        return self.f.read(size)
    def seekable(self):
        return True
    def close(self):
        self.f.close()

with File('/etc/passwd') as f:
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read(10))
    print(f.read

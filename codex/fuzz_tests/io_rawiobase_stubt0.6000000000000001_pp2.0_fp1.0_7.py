import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        if n >= 100:
            return self.f.read(n)
        return None
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return False

f = File(open('file.txt', 'rb'))
print(f.read(100))
print(f.read(100))
print(f.read(100))

class File2(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        if n >= 100:
            return self.f.read(n)
        return None
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return False

f = File2(open('file.txt', 'rb'))
print(f.read(100))
print(f.read(

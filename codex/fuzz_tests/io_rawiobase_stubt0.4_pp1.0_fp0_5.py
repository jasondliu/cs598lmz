import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None

    def open(self):
        self.file = open(self.path, 'rb')
        return self

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def read(self, n):
        return self.file.read(n)

file = File('/etc/hosts')
with file.open() as f:
    print(f.read(10))

class File:
    def __init__(self, path):
        self.path = path
        self.file = None

    def open(self):
        self.file = open(self.path, 'rb')
        return self.file

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

file = File('/etc/hosts')
with file.open() as f:
    print(f.read(10))

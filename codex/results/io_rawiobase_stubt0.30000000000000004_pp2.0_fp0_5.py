import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = None
    def open(self, mode='rb'):
        self.fd = open(self.name, mode)
    def close(self):
        self.fd.close()
    def read(self, n=-1):
        return self.fd.read(n)
    def write(self, b):
        return self.fd.write(b)
    def fileno(self):
        return self.fd.fileno()
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, type, value, traceback):
        self.close()

f = File('test.txt')
f.open()
print(f.read())
f.close()

with File('test.txt') as f:
    print(f.read())

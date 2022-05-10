import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def fileno(self):
        return self.f.fileno()
    def close(self):
        return self.f.close()

import sys
f = File(sys.stdout)
f.write(b'test')
f.close()

f = open('file.txt', 'r')
f = File(f)
f.read(4)
f.close()

import io
class File(io.IOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def close(self):
        return self.f.close()


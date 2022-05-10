import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        if n >= 0:
            return self.f.read(n)
        else:
            return self.f.read()
    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        b[:n] = data
        return n
    def write(self, b):
        return self.f.write(b)
    def close(self):
        return self.f.close()

def open(file, mode="r", buffering=-1, **kwargs):
    return io.IOBase(File(file), mode, buffering, **kwargs)

import sys
sys.modules["__main__"].open = open

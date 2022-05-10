import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b""
    def readable(self):
        return True
f = File()
print(f.read(1))

import io
import os
class File(io.RawIOBase):
    def __init__(self, f):
        self._f = f
    def read(self, n=-1):
        return self._f.read(n)
    def readable(self):
        return True
f = open(os.devnull, "rb")
f = File(f)
print(f.read(1))

class File(io.RawIOBase):
    def __init__(self, f):
        self._f = f
    def read(self, n=-1):
        return self._f.read(n)
    def readable(self):
        return True
f = open(os.devnull, "rb")
f = File(f)
print(f.read(1))

class File(io.RawIOBase):
    def __init__(self, f):
        self._f

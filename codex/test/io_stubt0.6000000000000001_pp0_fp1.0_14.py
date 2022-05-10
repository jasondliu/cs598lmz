import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

import gc; gc.collect()

print(view)

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[0] = ord('A')
    def readable(self):
        return True

f = io.BufferedReader(File())
print(f.read(1))
del f

import gc; gc.collect()

print(view)

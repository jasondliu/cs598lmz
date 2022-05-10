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
view

class File(io.RawIOBase):
    def read(self, size):
        global view
        view = bytearray(b'x' * size)
        return len(view)

f = io.BufferedReader(File())
f.read(1)
del f
view

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
        return len(buf)

f = io.BufferedReader(File())
f.read(1)
del f
view

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
assert view[0] == 0

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = memoryview(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
assert view[0] == 0

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = memoryview(buf[0])
    def readable(self):
        return True

f = io.BufferedReader(File())
buf = bytearray([0, 1, 2])
f.readinto(buf)
del f
assert view[0] == 0
assert view[1] == 1
assert view[2] == 2

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = memoryview(buf[1])
    def readable(self):
        return True

f = io.BufferedReader(File())
buf = byt

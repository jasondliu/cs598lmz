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

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[0] = 0
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f


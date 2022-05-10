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
    def readinto(self, buf):
        buf[:] = b"abc"
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
view

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b"abc"
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(2)
del f
view

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b"abc"
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(3)
del f
view

class File(io.RawIOBase):
    def readinto(self, buf):
        buf[:] = b"abc"
    def readable(self):
        return True

f = io.BufferedReader(File())


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
        global bview
        bview = bytes(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
bview

# Test __sizeof__

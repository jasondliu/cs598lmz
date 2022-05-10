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
        global view2
        view2 = buf
    def readable(self):
        return True

f = io.BufferedRWPair(File(), File())
f.read(1)
assert view == view2
del f

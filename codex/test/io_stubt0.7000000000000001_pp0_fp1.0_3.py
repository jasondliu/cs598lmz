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
if not view:
    raise Exception("readinto() did not call raw read")

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def read(self, size):
        return super().read(size)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

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
if view:
    raise Exception("readinto() was called when raw read returned None")

# Check that BufferedReader.readinto() is called on any object that
# implements it, even if it also implements read()
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
    raise Exception("readinto() was not called")

# Check that BufferedReader.readinto() is not called on any object that
# doesn't implement it,

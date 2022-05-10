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

print(view)

# io.TextIOBase

class File(io.TextIOBase):
    def read(self, size=-1):
        return "abc"
    def readable(self):
        return True

f = io.TextIOWrapper(File())


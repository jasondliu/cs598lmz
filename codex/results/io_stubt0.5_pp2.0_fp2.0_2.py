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

try:
    f.read(1)
except ValueError:
    print("ValueError")

try:
    view[0] = 0
except ValueError:
    print("ValueError")

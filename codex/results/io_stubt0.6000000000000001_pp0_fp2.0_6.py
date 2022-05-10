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

buf = bytearray(10)
with io.BufferedReader(File()) as f:
    f.readinto(buf)
del f

buf = bytearray(10)
with io.BufferedReader(File()) as f:
    f.readinto(buf)
    f.readinto(buf)
del f

buf = bytearray(10)
with io.BufferedReader(File()) as f:
    f.readinto(buf)
    f.readinto(buf)
    f.readinto(buf)
del f

buf = bytearray(10)
with io.BufferedReader(File()) as f:
    f.readinto(buf)
    f.readinto(buf)
    f.readinto(buf)
    f.readinto(buf)
del f

print(view)

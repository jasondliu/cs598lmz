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

for i in range(1000):
    s = memoryview(b"")
    s2 = s[0:1]

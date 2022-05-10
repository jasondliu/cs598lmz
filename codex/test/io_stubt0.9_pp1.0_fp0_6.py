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
a = []
del view
for i in range(10):
    a.append(i)

def zap():
    for i in range(10):
        del a[i]


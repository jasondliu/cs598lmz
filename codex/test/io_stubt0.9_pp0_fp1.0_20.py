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

del File
c = ''.join(map(chr, view[40:40+40]))
print(c)

del view

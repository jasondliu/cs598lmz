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

f = io.BufferedReader(File())
f.read(2)
del f

f = io.BufferedReader(File())
f.read(3)
del f

f = io.BufferedReader(File())
f.read(4)
del f

f = io.BufferedReader(File())
f.read(5)
del f

f = io.BufferedReader(File())
f.read(6)
del f

f = io.BufferedReader(File())
f.read(7)
del f

f = io.BufferedReader(File())
f.read(8)
del f

f = io.BufferedReader(File())
f.read(9)
del f

f = io.BufferedReader(File())
f.read(10)
del f

f = io.BufferedReader(File())
f.read(11)
del f

f = io.BufferedReader(File())
f.read(12)
del f

f = io.BufferedReader(File())


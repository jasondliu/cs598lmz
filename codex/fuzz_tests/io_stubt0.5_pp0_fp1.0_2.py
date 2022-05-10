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

f = io.BufferedReader(File())
f.read()
del f
print(view)

f = io.BufferedReader(File())
f.read(2)
del f
print(view)

f = io.BufferedReader(File())
f.read(0)
del f
print(view)

f = io.BufferedReader(File())
f.read(0)
del f
print(view)

f = io.BufferedReader(File())
f.read(3)
del f
print(view)

f = io.BufferedReader(File())
f.read(3)
del f
print(view)

f = io.BufferedReader(File())
f.read(4)
del f
print(view)

f = io.BufferedReader(File())
f.read(5)
del f
print(view)

f = io.BufferedReader(File())
f.read(6)
del f
print(view)

f = io.BufferedReader

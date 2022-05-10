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

# The same thing, but with a memoryview
f = io.BufferedReader(File())
f.read(1)
del f
print(view)

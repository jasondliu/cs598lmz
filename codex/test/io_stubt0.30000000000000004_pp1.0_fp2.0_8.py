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

# io.BufferedReader.readinto()

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.readinto(bytearray(1))
del f
print(view)

# io.BufferedReader.readinto1()

class File(io.RawIOBase):
    def readinto1(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())

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
f.read()
del f
f = io.BufferedReader(File())
f.read1()
del f
f = io.BufferedReader(File())
f.readinto1(bytearray(1))
del f
f = io.BufferedReader(File())
f.readinto(bytearray(1))

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = memoryview(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
f = io.BufferedReader(File())
f.read()
del f
f = io.BufferedReader(File())
f.read1()
del f
f = io.BufferedReader(File())
f.readinto1(bytearray(1))
del f
f = io.BufferedReader(File())
f.readinto(bytearray(1))

class File(io

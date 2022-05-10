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
print(sys.getrefcount(view))
# 2

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

buf = bytearray(2)
f = io.BufferedReader(File())
f.readinto(buf)
del f
print(sys.getrefcount(buf))
# 2

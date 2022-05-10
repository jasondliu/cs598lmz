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

print("eof: " + repr(view))
print("st_value: " + repr(st_value))
print("st_size: " + repr(st_size))
print("IndexOutOfBounds: " + repr(IndexOutOfBounds))

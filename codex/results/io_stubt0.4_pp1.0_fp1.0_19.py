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

# f is now a dangling pointer to a gc'ed object
# we need to ensure that the buffer is not invalidated
# when the object is destroyed

# this should not crash
view[0] = 1

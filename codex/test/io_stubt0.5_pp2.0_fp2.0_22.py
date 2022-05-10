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

# Test that the object is not deallocated.
view[0] = 0

# Test that the buffer is not deallocated.
view[1] = 0

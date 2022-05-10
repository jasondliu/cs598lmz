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

view[0] = 0

# test that the file is closed
try:
    f.read(1)
except ValueError:
    pass
else:
    raise Exception("f.read(1) didn't raise ValueError")

# test that the buffer is deallocated
view[0] = 0

# test that the file is closed after the buffer is deallocated
try:
    f.read(1)
except ValueError:
    pass
else:
    raise Exception("f.read(1) didn't raise ValueError")

# test that the buffer is deallocated after the file is closed
view[0] = 0

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

# Check that the buffer wasn't freed too early
view[0] = 0

# Check that the buffer wasn't freed too late
del view

# Check that the buffer wasn't freed twice
del view

print("ok")

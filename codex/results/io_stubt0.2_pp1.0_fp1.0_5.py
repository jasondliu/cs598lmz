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

# Test that the buffer is not freed.
view[0] = 0

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()

try:
    view[0] = 0
except ValueError:
    pass
else:
    raise Exception("buffer not freed")

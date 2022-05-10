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

# Test that the view is still alive
view[0] = 0

# Test that the buffer is cleared
f = io.BufferedReader(File())
f.read(1)
del f

# Test that the buffer is cleared
f = io.BufferedReader(File())
f.read(1)
f.read(1)
del f

# Test that the buffer is cleared
f = io.BufferedReader(File())
f.read(1)
f.read(1)
f.read(1)
del f

# Test that the buffer is cleared
f = io.BufferedReader(File())
f.read(1)
f.read(1)
f.read(1)
f.read(1)
del f

# Test that the buffer is cleared
f = io.BufferedReader(File())
f.read(1)
f.read(1)
f.read(1)
f.read(1)
f.read(1)
del f

# Test that the buffer is cleared

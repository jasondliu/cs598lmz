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

# Test that the buffer is still alive after the file is closed.
# This is important for the test that follows.
assert view

# Test that the buffer is released when the file is closed.
f = io.BufferedReader(File())
f.read(1)
del f

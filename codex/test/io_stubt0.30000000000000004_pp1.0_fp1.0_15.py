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

# This is what the buffer looks like after the file is closed.
# It's a bit hard to read, but it's a valid object.
view

# The buffer is still usable, but it's not a valid object.

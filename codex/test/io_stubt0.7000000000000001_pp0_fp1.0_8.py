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

# The view is still alive.
view[0] = 0x42

# This should crash, because the underlying file object
# doesn't support reading.
list(view)

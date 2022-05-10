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

# This used to crash when the buffer was deleted
# because the view was not updated to point to
# the new buffer.
view[0] = 1

# This also used to crash when the buffer was
# deleted because the weak reference to the
# buffer was not updated.
f = io.BufferedReader(File())
f.read(1)
del f

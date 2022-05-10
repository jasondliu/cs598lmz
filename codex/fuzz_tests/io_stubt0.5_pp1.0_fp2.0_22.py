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

# This should not throw an exception.
view.tobytes()

# Now, check that the array is still usable.
view[0] = b"a"
view.tobytes()

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

# The buffer shouldn't be deallocated yet because it's referenced from the
# buffer of the BufferedReader
print(view)

# Once the BufferedReader is destroyed, the buffer should be freed
del view

# This shouldn't crash
f = io.BufferedReader(File())
del f

# This shouldn't crash
f = io.BufferedReader(File())
f.read(1)
del f

# This shouldn't crash
f = io.BufferedReader(File())
f.read(1)
del f

# This shouldn't crash
f = io.BufferedReader(File())
f.read(1)
f.read(1)
del f

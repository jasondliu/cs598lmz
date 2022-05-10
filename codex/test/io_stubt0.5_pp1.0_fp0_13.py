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

view[0] = 42

# Verify that the buffer is not deallocated
# before the file is.
print(view[0])

# Check that the file is deallocated
# before the buffer is.
del view

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
view[0] = 0

# Test that the buffer is not deallocated if the file is still alive.
f = io.BufferedReader(File())
f.read(1)
del view

# Test that the buffer is deallocated if the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
del view

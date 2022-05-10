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

# Test that the buffer is not deallocated
view[0] = 0

# Test that the buffer is not deallocated, even if the file is closed
f = io.BufferedReader(File())
f.read(1)
f.close()
view[0] = 0

# Test that the buffer is not deallocated, even if the file is closed
# and the buffer is released
f = io.BufferedReader(File())
f.read(1)
f.close()
f.detach()
view[0] = 0

# Test that the buffer is not deallocated, even if the file is closed
# and the buffer is released and the buffer is deallocated
f = io.BufferedReader(File())
f.read(1)
f.close()
f.detach()
del view

# Test that the buffer is not deallocated, even if the file is closed
# and the buffer is released and the buffer is deallocated and the
# file is deallocated
f = io.BufferedReader(File())
f.read(1)

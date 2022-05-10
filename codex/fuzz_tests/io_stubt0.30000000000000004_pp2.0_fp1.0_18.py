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
view[0] = ord('x')

# Test that the buffer is not deallocated
del view

# Test that the buffer is not deallocated
view = None

# Test that the buffer is not deallocated
del view

# Test that the buffer is not deallocated
view = None

print('ok')

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

# Test that the buffer is not deallocated, and that the buffer
# is still usable.
print(view[0])
view[0] = b'x'[0]
print(view[0])

# Test that the buffer is not deallocated, and that the buffer
# is still usable.
del view
print(view[0])
view[0] = b'x'[0]
print(view[0])

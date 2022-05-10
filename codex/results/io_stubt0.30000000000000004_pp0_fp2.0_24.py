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

# Test that the buffer is not deallocated when the file is closed.
# This test is not very good, because it relies on the fact that
# the buffer is allocated in a specific way.

print(view[0])

# Test that the buffer is not deallocated when the file is closed.
# This test is not very good, because it relies on the fact that
# the buffer is allocated in a specific way.

print(view[0])

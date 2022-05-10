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

# Test that the buffer is not deallocated when the BufferedReader is
# destroyed.
print(view)
if view:
    print(view[0])
    if view[0] != 0:
        raise RuntimeError

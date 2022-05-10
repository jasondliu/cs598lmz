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

# Test that the file object is deallocated, even though a view
# is alive.
import gc
gc.collect()

# Test that the view is still alive.
print(view[0])

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

# Test that the buffer is not deallocated when the file is closed
# (the buffer is still referenced by the view).
import gc
gc.collect()

# Test that the buffer is deallocated when the view is deallocated.
del view
gc.collect()

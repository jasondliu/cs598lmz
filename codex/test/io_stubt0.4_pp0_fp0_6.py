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

# Check that the GC doesn't crash with a dangling reference to the
# buffer.
import gc
gc.collect()

# Check that the buffer was actually released.
import weakref

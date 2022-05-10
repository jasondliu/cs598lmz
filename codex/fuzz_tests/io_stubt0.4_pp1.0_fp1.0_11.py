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

# Test that the buffer was released.
import gc
gc.collect()

# If the buffer was released, then this will raise a ValueError.
view[0] = 0

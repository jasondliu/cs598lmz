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

# The buffer should not be deallocated, because it's still
# referenced by "view".
import gc
gc.collect()

# This should not crash.
view[0] = b'x'

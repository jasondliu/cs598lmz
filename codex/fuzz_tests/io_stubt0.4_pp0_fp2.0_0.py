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

# Exercise the garbage collector to ensure the file is closed
import gc
gc.collect()

# Check that the buffer is still alive
view.__array_interface__

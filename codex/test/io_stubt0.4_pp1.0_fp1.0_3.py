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

view[0] = ord('a')

# Check that the buffer was released.
import gc
gc.collect()
gc.collect()
if gc.garbage:
    print(gc.garbage)
    raise Exception("buffer not released")

# Check that the buffer can be reused.
f = io.BufferedReader(File())
f.read(1)
del f

# Check that the buffer wasn't reused.
if view[0] == ord('a'):
    raise Exception("buffer reused")

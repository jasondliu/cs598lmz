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

# Test that the Py_buffer is released.
import gc
gc.collect()

# Test that the view is still usable.
view[0] = 0
view[0]

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

# Test that the reference to the view is cleared
view = None
import gc
gc.collect()
gc.collect()
gc.collect()

# This used to crash
import weakref

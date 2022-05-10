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

import gc
gc.collect()

# Now we have a dangling reference to the buffer

# Exercise the GC to see if it is possible to trigger an
# assertion failure in debug builds
import sys
sys.getrefcount(view)

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

# Verify that view is not deallocated too early:
view[0] = 42

# Verify that it is deallocated when the last reference is removed
view = None
gc.collect()

# str is no longer referencing the buffer, so it is now safe to deallocate it
del str

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

if view[0] != ord('a'):
    raise RuntimeError("buf is not initialized from the parent object")

# check that the GC does not violate the buffer

import gc
gc.collect()
gc.collect()

if view[0] != ord('a'):
    raise RuntimeError("buf is not initialized from the parent object")

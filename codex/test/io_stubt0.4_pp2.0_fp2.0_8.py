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

# This used to crash in the deallocator of the buffered reader
# object because the raw object was already deallocated.
print(view)

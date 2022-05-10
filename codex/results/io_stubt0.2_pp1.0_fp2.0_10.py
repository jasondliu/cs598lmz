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

# The buffer should be released now.

import gc
gc.collect()

# Check that the buffer is still alive.

view[0] = ord('x')

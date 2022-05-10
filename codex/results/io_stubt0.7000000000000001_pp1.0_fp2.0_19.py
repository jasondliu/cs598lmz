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

# the following should raise an exception:
view[0] = 1
</code>
The bug is fixed in Python 3.6.


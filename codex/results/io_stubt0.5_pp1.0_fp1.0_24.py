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

view[0] = 1

import gc
gc.collect()

# This used to segfault.
# The problem was that the release of the Python object had
# a side-effect of decref'ing the buffer, which then triggered
# a call to PyObject_Free, which crashed.

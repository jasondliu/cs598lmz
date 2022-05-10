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

# This used to crash in the garbage collector, because the
# tp_clear handler for file objects would call PyObject_Free
# on the buffer, which is an invalid pointer (it's a slice
# of a bytearray).

# This test is adapted from issue #17724, where the problem
# was found.

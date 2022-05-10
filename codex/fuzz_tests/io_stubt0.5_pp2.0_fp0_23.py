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
# The buffer is now invalid, but the Py_buffer is still there.
# If the Py_buffer is freed, the GC will crash.

import gc
gc.collect()

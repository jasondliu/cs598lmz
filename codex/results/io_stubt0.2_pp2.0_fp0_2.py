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

# Issue #24078: the buffer of the BufferedReader was not released.
# It was only released when the BufferedReader was garbage collected.
# This test checks that the buffer is released when the BufferedReader
# is closed.
import gc
gc.collect()
print(view)

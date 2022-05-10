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
# This is the end of the monkeypatching, we can now use the gc
import gc
gc.collect()
# and the buffer should be freed.
print(view)

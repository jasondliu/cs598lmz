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

# test that the buffer was released
import gc
gc.collect()
assert view[0] == 0

# test that the buffer was released
import gc
gc.collect()
assert view[0] == 0

print("ok")

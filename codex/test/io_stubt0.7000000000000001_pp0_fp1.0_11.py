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

# We don't want to crash
print(view)

# We don't want to leak
import gc; gc.collect()
gc.collect()
print(gc.collect())

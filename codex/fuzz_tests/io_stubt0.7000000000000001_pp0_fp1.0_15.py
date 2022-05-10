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
gc.collect()

# GC the buffer and then try to read the old view.  This will crash if
# the buffer header has not been correctly updated.
f = io.BufferedReader(File())
print(f.read(1))

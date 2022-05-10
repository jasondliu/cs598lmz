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

# Check that the buffer was released
gc.collect()
gc.collect()
gc.collect()

if view:
    raise RuntimeError("buffer not released")

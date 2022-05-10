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

# Verify that the buffer was released.
gc.collect()
gc.collect()
gc.collect()
if view:
    raise Exception("buffer not released")

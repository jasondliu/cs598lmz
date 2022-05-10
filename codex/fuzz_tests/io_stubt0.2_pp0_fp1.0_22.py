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

# Test that the buffer is not freed until the file is closed.
gc.collect()
gc.collect()
gc.collect()

# The buffer should be freed now.
gc.collect()
gc.collect()
gc.collect()

# Check that the buffer is freed.
if view:
    raise Exception("buffer not freed")

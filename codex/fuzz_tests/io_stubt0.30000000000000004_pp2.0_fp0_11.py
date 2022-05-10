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

# Check that the buffer was released.
gc.collect()
if view:
    raise Exception("buffer not released")

# Check that the buffer is released when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
del f
gc.collect()
if view:
    raise Exception("buffer not released")

# Check that the buffer is released when the file is deleted.
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
if view:
    raise Exception("buffer not released")

# Check that the buffer is released when the file is closed and deleted.
f = io.BufferedReader(File())
f.read(1)
f.close()
del f
gc.collect()
if view:
    raise Exception("buffer not released")

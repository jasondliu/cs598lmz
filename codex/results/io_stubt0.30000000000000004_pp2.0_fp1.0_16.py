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

# Check that the buffer is not freed by the GC
gc.collect()

# Check that the buffer is freed when the file is closed
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()

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

# The buffer should have been released when the BufferedReader was
# deleted, but it wasn't.  This caused a segfault when the buffer was
# garbage collected.
gc.collect()

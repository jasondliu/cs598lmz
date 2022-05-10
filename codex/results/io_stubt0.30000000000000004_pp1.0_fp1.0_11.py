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

view[0] = 0

# Test that the buffer is not deallocated after the file is closed.
# This is a regression test for https://bugs.python.org/issue27097
# where the buffer was deallocated because the file was closed.
# The buffer is now kept alive by the weakref in the file object.
gc.collect()

# Test that the buffer is deallocated after the file is gone.
del view
gc.collect()

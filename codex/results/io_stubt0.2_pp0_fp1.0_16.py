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

# The view should not be freed until the file is closed.
gc.collect()
gc.collect()
gc.collect()

# The view should be freed now.
del view
gc.collect()
gc.collect()
gc.collect()

# Check that the file is closed.
try:
    f.read(1)
except ValueError:
    pass
else:
    raise Exception("file is not closed")

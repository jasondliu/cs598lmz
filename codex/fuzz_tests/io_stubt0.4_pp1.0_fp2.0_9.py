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

del view

# Test that the file object is closed when the BufferedReader is
# garbage collected.
class File(io.RawIOBase):
    def __init__(self):
        self.closed = False
    def close(self):
        self.closed = True
    def readable(self):
        return True

f = io.BufferedReader(File())
del f
gc.collect()
assert f.closed

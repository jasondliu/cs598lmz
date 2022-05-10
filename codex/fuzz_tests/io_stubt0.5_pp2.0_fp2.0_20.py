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
assert view is None

# Test that the destructor runs when the wrapped object is freed.
class File(object):
    def readable(self):
        return True
    def close(self):
        global view
        view = None
f = io.BufferedReader(File())
del f
gc.collect()
gc.collect()
assert view is None

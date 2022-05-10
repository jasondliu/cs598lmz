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
del File

# Check that the reference to the view is gone.
gc.collect()
assert not gc.is_tracked(view)

# Check that the reference to the underlying buffer is gone.
gc.collect()
assert not gc.is_tracked(buf)

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

# Make sure the buffer is not freed.
if len(view) != 1:
    raise RuntimeError("Buffer freed")

# Test that the buffer is released when the reference count reaches 0.
f = io.BufferedReader(File())
f.read(1)
del f
del view

# Test that the buffer is released when the reference count reaches 0,
# even if the buffer is not the first item in the tuple.
f = io.BufferedReader(File())
f.read(1)
view = f.read(1)
del f
del view

# Test that the buffer is released when the reference count reaches 0,
# even if the buffer is not the first item in the tuple.
f = io.BufferedReader(File())
f.read(1)
view = f.read(1)
del view
del f

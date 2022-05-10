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

# Check that the buffer was released when the reader was closed.
assert view.obj is None

# Check that the buffer was released when the reader was deleted.
view = None
f = io.BufferedReader(File())
f.read(1)
del f
assert view.obj is None

# Check that the buffer was released when the reader was closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
assert view.obj is None

# Check that the buffer was released when the reader was deleted.
f = io.BufferedReader(File())
f.read(1)
del f
assert view.obj is None

# Check that the buffer was released when the reader was closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
assert view.obj is None

# Check that the buffer was released when the reader was deleted.
f = io.BufferedReader(File())
f.read(1)
del f
assert view.obj is None

# Check that the buffer was released when

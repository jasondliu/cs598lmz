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

# The buffer should not be freed until the file is closed.
gc.collect()
assert view[0] == 0

# The buffer should be freed when the file is closed.
del view
gc.collect()

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
del f
gc.collect()

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f = None
gc.collect()

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f = 0
gc.collect()

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)


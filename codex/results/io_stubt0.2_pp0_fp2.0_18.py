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

# Test that the buffer is not freed before the file is closed.
gc.collect()

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
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
f.close()
del f
gc.collect()

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
del f
gc.collect()

# Test that the buffer is freed when the file

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

# Test that the buffer is not deallocated when the file is still alive.
gc.collect()

# Test that the buffer is deallocated when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
gc.collect()

# Test that the buffer is deallocated when the file is garbage collected.
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()

# Test that the buffer is deallocated when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
gc.collect()

# Test that the buffer is deallocated when the file is garbage collected.
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()

# Test that the buffer is deallocated when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
gc.collect()

# Test that the buffer is

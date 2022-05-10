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

# Test that the buffer is not deallocated while the file is alive
gc.collect()

# Test that the buffer is deallocated when the file is closed
del view
gc.collect()

# Test that the buffer is deallocated when the file is closed
# even if the buffer is referenced by a different name
view = f
del f
gc.collect()

# Test that the buffer is deallocated when the file is closed
# even if the buffer is referenced by a different name
view = f
del f
gc.collect()

# Test that the buffer is deallocated when the file is closed
# even if the buffer is referenced by a different name
view = f
del f
gc.collect()

# Test that the buffer is deallocated when the file is closed
# even if the buffer is referenced by a different name
view = f
del f
gc.collect()

# Test that the buffer is deallocated when the file is closed
# even if the buffer is referenced by a different name
view = f
del f
gc.collect()

# Test that the buffer is de

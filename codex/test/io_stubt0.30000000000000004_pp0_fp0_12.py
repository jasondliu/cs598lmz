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

# Test that the buffer is not freed when the file is closed.
import gc
gc.collect()
gc.collect()
gc.collect()
print(view)

# Test that the buffer is freed when the file is deleted.
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
gc.collect()
gc.collect()
print(view)

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
gc.collect()
gc.collect()
gc.collect()
print(view)

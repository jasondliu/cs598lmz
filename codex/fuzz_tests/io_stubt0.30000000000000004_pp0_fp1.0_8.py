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

# Test that the buffer is freed when the last reference to the
# BufferedReader is deleted.
import gc
gc.collect()
gc.collect()
gc.collect()

# Test that the buffer is freed when the BufferedReader is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()

gc.collect()
gc.collect()
gc.collect()

# Test that the buffer is freed when the BufferedReader is deleted.
f = io.BufferedReader(File())
f.read(1)
del f

gc.collect()
gc.collect()
gc.collect()

# Test that the buffer is freed when the BufferedReader is garbage
# collected.
def test_gc():
    f = io.BufferedReader(File())
    f.read(1)

test_gc()
gc.collect()
gc.collect()
gc.collect()

# Test that the buffer is freed when the BufferedReader is closed.
f = io.BufferedReader(File())
f.read(1)


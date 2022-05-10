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

# Test that the buffer was freed
import gc
gc.collect()

# Test that the buffer is still valid
view[0] = ord('a')

# Test that the buffer is still valid after a GC
gc.collect()
view[0] = ord('b')

# Test that the buffer is still valid after a GC
gc.collect()
view[0] = ord('c')

# Test that the buffer is still valid after a GC
gc.collect()
view[0] = ord('d')

# Test that the buffer is still valid after a GC
gc.collect()
view[0] = ord('e')

# Test that the buffer is still valid after a GC
gc.collect()
view[0] = ord('f')

# Test that the buffer is still valid after a GC
gc.collect()
view[0] = ord('g')

# Test that the buffer is still valid after a GC
gc.collect()
view[0] = ord('h')

# Test that the buffer is still valid after a GC
gc.collect()

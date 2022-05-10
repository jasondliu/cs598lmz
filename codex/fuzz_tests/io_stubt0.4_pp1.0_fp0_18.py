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

print(view)
del view

# Test that a weakref to the buffer is not kept
import weakref
wr = weakref.ref(view)
del view
print(wr())

# Test that the buffer is not kept alive by the GC
import gc
gc.collect()
print(wr())

# Test that the buffer is not kept alive by the GC
import gc
gc.collect()
print(wr())

# Test that the buffer is not kept alive by the GC
import gc
gc.collect()
print(wr())

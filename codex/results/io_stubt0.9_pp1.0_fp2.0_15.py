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
# The buffer was not recycled; refcount was 1
gc.collect()
print(len(view))
# The buffer was recycled
print(gc.collect())

# No free list.
f = io.BufferedReader(File(), buffer_size=1)
f.readinto(bytearray(1))
del f
gc.collect()
print(gc.collect())

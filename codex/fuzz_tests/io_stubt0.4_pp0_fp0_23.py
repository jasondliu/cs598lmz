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

# The buffer should be deallocated on the next GC
for i in range(10):
    gc.collect()

# But it should still be accessible
print(view[0])

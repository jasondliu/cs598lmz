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

# trigger GC
for i in range(10):
    _ = bytearray(1)

gc.collect()

# Check that it did not garbage collect the bytearray
view[0] = 5

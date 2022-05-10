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
view  # [42]

# The 1-byte buffer is now owned by the reference to File.readinto(),
# and is not freed.

# To avoid this, set buf = memoryview(buf) in File.readinto().

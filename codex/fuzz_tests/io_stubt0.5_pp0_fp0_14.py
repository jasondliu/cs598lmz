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
gc.collect()

# Verify that the buffer is still alive
view[0] = 0

# Check that the buffer is the same
assert view == bytearray(b'\x00')

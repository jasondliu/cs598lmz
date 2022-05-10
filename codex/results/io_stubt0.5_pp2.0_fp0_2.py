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

# Check for buffer overflow
view[0] = 0xFF

# Check for buffer underflow
view[-1] = 0xFF

# Check for buffer overflow
view[1] = 0xFF

# Check for buffer underflow
view[-2] = 0xFF

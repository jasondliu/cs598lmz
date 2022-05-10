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

# f is now a regular buffer with a dangling pointer
import struct
struct.unpack_from('B', view, 0) # SEGV

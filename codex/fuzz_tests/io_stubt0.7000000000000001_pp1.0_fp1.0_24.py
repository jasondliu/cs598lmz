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
</code>

The issue seems to be that <code>PyBuffer_Release</code> doesn't decrement the reference count of the underlying buffer, so it gets collected and the pointer is invalidated.
The other possibility is that the interaction between <code>PyBuffer_Release</code> and <code>releasebuffer</code> is wrong.


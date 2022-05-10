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

# This is a bit of a hack, but it's the only way to get a pointer to the
# buffer.
import ctypes
buf = ctypes.cast(id(view), ctypes.POINTER(ctypes.c_char))

# Now we can use the buffer as a string.
print(buf[0])
buf[0] = b'a'[0]
print(buf[0])

# We can also use the buffer as an array.
buf[1] = b'b'[0]
buf[2] = b'c'[0]
print(view)

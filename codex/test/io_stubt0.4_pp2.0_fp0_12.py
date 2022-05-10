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

# io.BufferedReader.readinto is not implemented, so it calls
# io.RawIOBase.readinto, which calls the underlying object's readinto
# method.  That method is File.readinto, which sets a global variable
# to the buffer.  The buffer is then deleted, but the global variable
# is still alive.  The next time the buffer is used, it crashes.

# This is a bug in CPython.  It should free the buffer before calling
# the readinto method.

# This is a bug in PyPy.  It should not free the buffer at all.

# This is a bug in both.  The buffer should be allocated as a
# writable buffer.

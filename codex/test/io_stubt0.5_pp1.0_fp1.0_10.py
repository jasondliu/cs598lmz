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

# io.BufferedReader.__init__() calls io.RawIOBase.readinto()
# to fill the buffer.  This is a problem in general, but it
# is particularly bad when the buffer is large, because
# the readinto() call allocates a new buffer and copies
# the entire buffer into it.

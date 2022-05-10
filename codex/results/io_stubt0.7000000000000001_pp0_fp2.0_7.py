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

# The above code uses a file-like object with a readinto method. When
# the BufferedReader is garbage-collected, its buffer is freed, but
# the buffer is still referenced by the 'view' global variable. This
# can lead to a segfault if the buffer is then written to.

# Uncomment the following line to see the problem.
view[0] = 1

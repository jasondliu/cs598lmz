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

# In Python 2.6, the above code would crash as soon as the File object was
# destroyed.  The reason is that the view was still referencing the
# underlying buffer, and the underlying buffer would be destroyed while the
# view was still alive.

# The following code is a workaround for the bug.  It doesn't crash, but it
# leaks memory.  The workaround is to avoid the situation where the view is
# still alive after the underlying buffer has been destroyed.  This is
# accomplished by making sure that the view is destroyed before the buffer.
# In this case, it is accomplished by making sure that the view is destroyed
# before the File object is destroyed.

import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del view
del f

# The following code is a workaround for the workaround.  It doesn't crash,
# and it doesn't leak memory.  The workaround is to make

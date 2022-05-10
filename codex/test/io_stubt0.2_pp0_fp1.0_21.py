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

# This is a test for a bug in the implementation of
# BufferedReader.__init__.  It failed with a segfault.

# This is a test for a bug in the implementation of
# BufferedReader.__init__.  It failed with a segfault.

# This is a test for a bug in the implementation of
# BufferedReader.__init__.  It failed with a segfault.

# This is a test for a bug in the implementation of
# BufferedReader.__init__.  It failed with a segfault.

# This is a test for a bug in the implementation of
# BufferedReader.__init__.  It failed with a segfault.

# This is a test for a bug in the implementation of
# BufferedReader.__init__.  It failed with a segfault.

# This is a test for a bug in the implementation of
# BufferedReader.__init__.  It failed with a segfault.

# This is a test for a bug in the implementation of
# Buff

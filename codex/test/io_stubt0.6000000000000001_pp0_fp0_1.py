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

# File objects should be closed when they are collected, but they
# don't close the underlying buffer.
# This test is only meaningful if the underlying buffer is the view
# buffer (otherwise it will be closed by the BufferedReader).
view = None

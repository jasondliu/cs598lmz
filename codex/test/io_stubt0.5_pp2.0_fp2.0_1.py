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

# This is a Python 2.7 bug, where the deallocator for
# BufferedReader calls the deallocator for File, which
# then calls the deallocator for view.  This is fixed
# in Python 3.

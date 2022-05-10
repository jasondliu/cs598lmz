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

# This used to cause a segfault because the Python file object was
# finalized while the underlying C++ file object was still in use.

# This test is a bit fragile, because it relies on the fact that the
# Python file object is finalized before the underlying C++ file
# object.  This is a bit of a hack...

print(view)

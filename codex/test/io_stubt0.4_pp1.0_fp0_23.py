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

view[0] = ord('a')

# Test that the reference count of the underlying file object is
# decremented when the buffered reader is deleted.

import sys
if sys.getrefcount(view) != 2:
    print("underlying file object not freed")

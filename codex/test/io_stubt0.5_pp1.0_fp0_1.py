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

# The above code will leak a reference to the view object.
# This test checks that the reference is released when the
# BufferedReader is deleted.

import gc

gc.collect()
if view is not None:
    print("Leaked reference to view")
    print(view)

# The above code will also leak a reference to File (the
# raw io object). This test checks that the reference is
# released when the BufferedReader is deleted.

class File:
    def __del__(self):
        global f
        f = None

f = File()

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

# Make sure the storage is freed
view = None
import gc; gc.collect()

# Now create a new file object, write to it, then close it.
# The allocated storage should be freed when the file is closed.

f = io.BufferedWriter(File())
f.write(b"xyz")
del f

import gc; gc.collect()

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

# Verify that the buffer was deallocated when the file was closed.
assert sys.getrefcount(view) == 1

import gc
gc.collect()

assert sys.getrefcount(view) == 1

# This test will fail if the buffer is not deallocated.
class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)

# Verify that the buffer was deallocated when the file was closed.
assert sys.getrefcount(view) == 1

import gc
gc.collect()

assert sys.getrefcount(view) == 1

# Issue #6127: readinto() failed to release the GIL.
class File(io.RawIOBase):
    def readinto(self, buf):
        for i in range(len(buf)):
            buf[i] = ord("a")
    def readable(self):
        return True

f =

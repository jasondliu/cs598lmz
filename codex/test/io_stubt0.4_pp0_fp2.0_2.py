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

import gc
gc.collect()

view[0] = 1

# This is a test for http://bugs.python.org/issue17658
# Make sure that the buffer is not freed before the buffer object
# is freed.

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

import gc
gc.collect()

# Test that the buffer is released when the file is closed.

import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
f.close()

import gc
gc.collect()

view[0] = 1

# Test that the buffer is released when the file is closed
# with
